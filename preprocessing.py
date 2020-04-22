def check_measure_validity(df, measures):
    invalid_measures = []
    for i in range(len(measures)-1):
        snippet = df.loc[measures[i]+1: measures[i+1]-1]
        if snippet['**recip'].sum() != meter[0] : invalid_measures.append(df['**recip'].loc[measures[i]]) 
    return invalid_measures


def handle_metadata(df, metadata):
    if metadata:
        tempo = int(df['**recip'][df['**recip'].apply(lambda x: '*MM' in x)].unique()[0].strip('*MM')) 
        meter = tuple(map(lambda x: int(x), \
                         df['**recip'][df['**recip'].apply(lambda x: '/' in x)].unique()[0].strip('*M').split('/')))
    else:
        tempo = 95
        meter = (4,4)
    return (tempo, meter)


def handle_pickup(df, pickup_control):
    pickup = False        
    if pickup_control:
        if (df['**recip'] == '=0').any():
            pickup = True
            pickup_start = df[df['**recip'].apply(lambda x: x == '=0')].index
            pickup_end = df[df['**recip'].apply(lambda x: x == '=1')].index

            for i, idx in enumerate(pickup_start):
                snippet = df.loc[idx+1:pickup_end[i]-1]
                snippet['**recip'][snippet['**lyrics']=='.'] = 0
                rest = meter[0] - snippet['**recip'][snippet['**lyrics']!='.'].sum()
                snippet['**recip'].at[idx+1] = rest
    return df, pickup


def _convert_recip(string, ref):
    if '=' in string:
        return string
    elif '%' in string:
        (num,coef) = list(map(lambda x: int(x), string.split('%')))
        return coef * ref / num
    else:    
        dots = string.count('.')
        num = int(string.strip('.'))
        coef = 1
        for d in range(dots):
            coef += 1 / (2**(d+1))

        return coef * ref / num
        

class HumdrumSummary():
    def __init__(self, sample_path, metadata=True, pickup_control=True):

        raw_df =  pd.read_table(sample_path)
        df = raw_df[raw_df['**recip'].apply(lambda x: '!' not in x)]   

        tempo, meter = handle_metadata(df, metadata)

            
        measures = df[df['**recip'].apply(lambda x: '=' in x)].index
        
        df = df[df['**recip'].apply(lambda x: x[0] in '0123456789=')]
        df['**recip'] = df['**recip'].apply(lambda x: _convert_recip(string=x,ref=meter[1]))             
        df, pickup = handle_pickup(df, pickup_control)
        
        invalid_measures = check_measure_validity(df, measures)#invalid_measures    

        df = df[df['**recip'].apply(lambda x: type(x) != str)]
        df = df[df['**recip'] != 0]
        df['cum_recip'] = df['**recip'].cumsum()
        df['breakpoints'] = df['cum_recip'][df['**break'].apply(lambda x: x in ['3','4'])].apply(lambda x: (x- df['**recip'].min()/4)%4)
        
        self.pickup = pickup
        self.measure = df['**recip'].sum() / meter[0]
        self.meter = meter
        self.tempo = tempo
        self.df = df
        self.raw_df = raw_df
        self.syl_onsets = df[df['**lyrics']!='.'].shape[0]
        self.syllabic_rate = tempo / (60 * df['**recip'][df['**lyrics']!='.'].mean())
        self.rhyme = df[df['**rhyme']!='.'].cum_recip.apply(lambda x: (x-df['**recip'].min()/4)%4)
        self.MC = sample_path.split('/')[-1].split('_')[0]
        self.breakpoints = df['breakpoints']
        self.invalid_measures = invalid_measures
        self.lang = sample_path.split('/')[1]
        
        self.rhyme_entropy = entropy(self.rhyme)
        self.breakpoints_entropy = entropy(df['breakpoints'].dropna())

        