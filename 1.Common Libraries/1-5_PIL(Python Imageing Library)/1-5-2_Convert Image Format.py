from PIL import Image
def  IsValidImage(img_path):
    """"
    判斷檔案是否為有效(完整)的圖片
    ：parm img_path：圖片路徑
    ：return：Ture：有效 Flase：無效
    """
    bValid = True
    try:
        Image.open(img_path).verify()
    except:
        bValid = False
    return bValid

def transimg(img_path):
    """
    轉換圖片格式
    ：parm img_path：圖片路徑
    ：return：Ture：成功 Flase：失敗
    """    
    if IsValidImage(img_path):
        try:
            str = img_path.rsplit(".",1)    #找到 . 當做分界點，分成兩個字串
            output_img_path = str[0] + ".jpg"
            print(output_img_path)
            im = Image.open(img_path)
            im.save(output_img_path)
            return True
        except :
            return False
    else:
        return False
    
if __name__ == "__main__":
    img_path = (r"D:\pyrhon_test\1.Common Libraries\Lenna.bmp")
    print(transimg(img_path))