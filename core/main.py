import os
import backend
import fera_components

def refresh() :
    print("Polling Fera Backend from server : ")
    fera_components.refresh()