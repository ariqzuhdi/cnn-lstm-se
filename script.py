import pandas as pd

def filtering(csv):
    df = pd.read_csv(csv)

    df_cleaned = df.dropna()

    # Simpan hasil ke file CSV baru (atau timpa file lama)
    if i == 1:
        df_cleaned.to_csv('cleanup_data.csv', index=True)
    else:
        df_cleaned.to_csv('cleanup_data.csv', mode='a', header=False, index=True)

    df = pd.read_csv('cleanup_data.csv')

    # Filter hanya baris dengan detik bernilai 0 (menunjukkan menit penuh)
    df_specified_MMSI = df[df['MMSI'] == 247320400]

    # Simpan hasil ke file CSV baru
    if i == 1: 
        df_specified_MMSI.to_csv('train_data.csv', index=True)
    else:
        df_specified_MMSI.to_csv('train_data.csv', mode='a', header=False, index=True)

    print("Succeeded")

for i in range(1, 32):
    if i < 10:
        filtering("AIS_2023_12_0" + str(i) + ".csv")
        print("Succeed " + str(i))
    else:
        filtering("AIS_2023_12_" + str(i) + ".csv")
        print("Succeed " + str(i))