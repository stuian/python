def main():
    try:
        with open("yoghourt.png",'rb') as f:
            data = f.read()
        with open('yoghourt2.png','wb') as f2:
            f2.write(data)
    except FileNotFoundError as e:
        print("指定的文件无法打开.")
    except IOError as e:
        print("读写文件是出现错误.")
    print("程序执行结束.")

if __name__ == '__main__':
    main()