import pandas as pd
from tqdm import tqdm


def generate_final_data(job_title, raw_data_path, save_path):
    df = pd.read_csv(job_title)
    dict_ = {}
    for i in range(0, len(df['tier2'])):
        dict_[df['job_name'][i]] = str(df['tier2'][i].strip("\"").lstrip("\[").rstrip("\]").strip("\'").replace('\'', '').replace('‘', '').replace('’', ''))

    dict_tier_convert = {}
    for i in range(0, len(df['tier1'])):
        line = str(df['tier2'][i].strip("\"").lstrip("\[").rstrip("\]").strip("\'").replace('\'', '').replace('‘', '').replace('’', ''))
        dict_tier_convert[line] = str(df['tier1'][i])

    f = open(raw_data_path)
    reader = pd.read_csv(f, sep=',', iterator=True)
    loop = True
    chunkSize = 100000
    chunks = []
    while loop:
        try:
            chunk = reader.get_chunk(chunkSize)
            chunks.append(chunk)
        except StopIteration:
            loop = False
            print("Iteration is stopped.")
    df2 = pd.concat(chunks, ignore_index=True)
    print(df2.shape)

    job_list = []
    for i in range(0, len(df2['jobCate'])):
        try:
            job_list.append(dict_[df2['jobCate'][i]])
        except Exception as e :
            job_list.append("")
    df2['tier2-position'] = job_list

    tier1_list = []
    for i in range(0, len(df2['tier2-position'])):
        try:
            tier1_list.append(dict_tier_convert[df2['tier2-position'][i]])
        except Exception as e:
            tier1_list.append("")
    df2['tier1-position'] = tier1_list
    df2.rename(columns = {"jobCate": "tier3-position"}, inplace=True)
    df2['id'] = [i for i in range(len(df2))]
    df2 = df2[df2['tier2-position'] != '']
    df2.rename(columns={"tier3-position": "tier_third_position"}, inplace=True)
    df2.rename(columns={"tier2-position": "tier_second_position"}, inplace=True)
    df2.rename(columns={"tier1-position": "tier_first_position"}, inplace=True)
    df2[['jobSalary_format']] = df2[['jobSalary_format']].apply(pd.to_numeric)
    new_df = df2[['id', 'incName', 'tier_first_position', 'tier_second_position', 'tier_third_position', 'jobDiploma', 'jobSalary',
                  'jobSalary_format', 'jobSalary_range', 'jobWorkAge', 'jobWorkCity_format', 'jobWorkProvince', 'jobDesc']]
    print('lenght of final data', len(new_df))
    new_df.to_csv(save_path, index=False)
    return new_df


if __name__ == '__main__':
    save_file_path = './final_data.csv'
    job_title_info = './new_tier1-tier2-tier3.csv'
    raw_data = './all_data.csv'
    generate_final_data(job_title_info, raw_data, save_file_path)