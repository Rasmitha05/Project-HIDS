import numpy as np 
import pandas as pd
import pickle
import csv


def modelp(inputtxt):
    df = pd.DataFrame([line.split(',') for line in inputtxt.splitlines()])
    df.to_csv('inputdf.csv', index=False)
    
    imputer = pickle.load(open('imputer.pkl','rb'))
    scaler = pickle.load(open('scaler.pkl','rb'))
    encoder = pickle.load(open('encoder.pkl','rb'))
    model = pickle.load(open('model.pkl','rb'))
    main_df = pd.read_csv('inputdf.csv')
    
    main_df.columns=[
    'srcip',
    'sport',
    'dstip',
    'dsport',
    'proto',
    'state',
    'dur',
    'sbytes',
    'dbytes',
    'sttl',
    'dttl',
    'sloss',
    'dloss',
    'service',
    'Sload',
    'Dload',
    'Spkts',
    'Dpkts',
    'swin',
    'dwin',
    'stcpb',
    'dtcpb',
    'smeansz',
    'dmeansz',
    'trans_depth',
    'res_bdy_len',
    'Sjit',
    'Djit',
    'Stime',
    'Ltime',
    'Sintpkt',
    'Dintpkt',
    'tcprtt',
    'synack',
    'ackdat',
    'is_sm_ips_ports',
    'ct_state_ttl',
    'ct_flw_http_mthd',
    'is_ftp_login',
    'ct_ftp_cmd',
    'ct_srv_src',
    'ct_srv_dst',
    'ct_dst_ltm',
    'ct_src_ ltm',
    'ct_src_dport_ltm',
    'ct_dst_sport_ltm',
    'ct_dst_src_ltm'
    ]
    
    main_df['ct_flw_http_mthd'] = main_df['ct_flw_http_mthd'].replace(np.nan,0,regex=True)
    main_df['ct_ftp_cmd'] = main_df['ct_ftp_cmd'].replace(" ","0",regex=True)
    main_df['is_ftp_login'] = main_df['is_ftp_login'].replace(np.nan,0,regex=True)
    main_df  = main_df.replace('-','unkown',regex=True)
    main_df['ct_ftp_cmd'] = main_df['ct_ftp_cmd'].apply(pd.to_numeric)
    
    main_df = main_df.drop(['sport','dsport'],axis = 1)
    
    input_cols = list(main_df.columns[0:-2])
    
    numeric_cols = main_df.select_dtypes(include = np.number).columns.tolist()[:]
    categorical_cols = main_df.select_dtypes('object').columns.tolist()
    
    main_df[numeric_cols] = imputer.transform(main_df[numeric_cols])
    main_df[numeric_cols] = scaler.transform(main_df[numeric_cols])
    
    
    encoded_cols = list(encoder.get_feature_names_out(categorical_cols))
    encoded_main_df = pd.DataFrame(encoder.transform(main_df[categorical_cols]).toarray(), columns=encoded_cols)
    main_df = pd.concat([main_df,encoded_main_df],axis= 1)
    
    main_df = main_df.drop(categorical_cols,axis=1)
    
    main_df.sort_index(axis=1,inplace=True)
    
    result= model.predict(main_df)[0]
    return result