from spydagram import _cli_entrypoint
# Entrypoint if run in module mode 
# i.e. if used as an 'executable' this will 
# enter and the cli entrypoint function will be run  

def main():
    _cli_entrypoint()

if __name__ == "__main__":
    main()