from netstat import netstat as nst

def main():
    nst.get_local_ports(10, 70000)
    nst.get_listening_ports(10, 70000)



if __name__ == "__main__":
    main()