import fera_components as fera

FeraServerAddress = input("Address of your Fera Server : ")

def refresh() :
    print("Refreshing Backend for FERA SERVER : " + FeraServerAddress)
    fera.refresh(FeraServerAddress)