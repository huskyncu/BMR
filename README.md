# BMR Project
###### tags: `合太醬`
###### tags: `家教`
github
## 題目
病患資料資料庫系統

## 說明：
請撰寫一個資料庫系統，讓使用者可以操作。
程式開始頁面會有圖形化介面讓使用者選擇服務(新增/查詢/刪除/更新/結束程式)。
接著並外接第三方資料庫或資料表。
以下是程式主要操作流程：
### 新增資料
* 使用者可以輸入以下資訊以新增(建立)資料：
    * 名字
    * 身分證字號
    * 年紀
    * 性別
    * 體重
    * 身高
* 接著電腦會計算出並告知使用者以下數據
    * bmi
    * bmi 判定體位
    * 以身高與bmi 計算理想體重
    * 體脂率
    * 體脂率判定體位
* 接著將數據新增進資料庫，可告知使用者輸入成功！

### 查詢資料
* 請使用者輸入名字跟身份證字號查詢該使用者資料。
* 查詢到使用者，需輸出：
    * 名字
    * 身分證字號
    * 年紀
    * 性別
    * 體重
    * 身高
    * bmi
    * bmi 判定體位
    * 以身高與bmi 計算理想體重
    * 體脂率
    * 體脂率判定體位
* 如果==沒有這個人的資料==，要告知使用者==查無此人==。

### 更新資料
* 先輸入姓名看要修改誰的資料
* 如果==沒有這個人的資料==，要告知使用者==查無此人==。
* 使用者可以重新輸入以下資訊以更新資料：
    * 危險因子
    * 年紀
    * 性別
    * 藥物
    * 劑量
    * 部位

### 刪除資料
* 請使用者輸入名字以刪除該使用者資料。
* 如果==沒有這個人的資料==，要告知使用者==查無此人==。

### 結束程式
就結束程式。

## 體位公式：

### BMI

* $BMI=\frac{體重(kg)}{(身高(cm))^2}$
* BMI與體位對照
    * 過輕（BMI<18.5 kg/m²）
    * 健康體重(理想體重)（18.5 kg/m²≦BMI<24 kg/m²）
    * 過重（24 kg/m²≦BMI<27 kg/m²）
    * 肥胖（BMI≧27 kg/m²）
* 理想體重
    * 最輕：$18.5\times (身高(公尺))^2$ 
    * 最重：$24\times(身高(公尺))^2$


### BMR

* $BMR=1.2\times bmi+ 0.23 \times 年齡 - 5.4 - 10.8\times(2-性別)$ 算出來單位是百分比(%)。
    * 性別部分，男生是1，女生是2
* BMR與體位對照表
![](https://i.imgur.com/Nk8EHEy.png)

## basic feature demo 

{%youtube 4QG7JpTifTI %}
https://youtu.be/4QG7JpTifTI

## bonus feature demo 

{%youtube 7ePlqHmckO4 %}
https://www.youtube.com/watch?v=7ePlqHmckO4

## 評分標準

### Basic Feature 100 pts. 



| 實作內容               | 使用程式概念 | 分數 |
| ---------------------- | ------------ | :----: |
| 有註解                 | #            | 10   |
| 能重複給使用者選擇服務 | while 迴圈,if  | 10   |
| 能夠輸入個人資料 與 印出對應資料     | input(), print()      | 10   |
| 存取檔案       |  txt/csv/excel   |  10 |
| 計算bmi      | operate, if | 5   |
| 判定bmi 體位      | operate, if | 5   |
| 計算理想體重      | operate, if | 5   |
| 計算bmr      | operate, if | 5   |
| 判定bmr 體位      | operate, if | 5   |
| 新增資料庫個人資料      |   file open/dict     |  5   |
| 查詢資料庫個人資料   |   file read/dict |   5  |
| 刪除特定資料     | 陣列/dict/file     | 5 |
| 修改特定資料     | 陣列/dict/file     | 5 |
| 有使用function操作 |def  | 5|
| 有使用自訂模組操作 |import  | 5|
| 防呆設計/例外處理         |  if 判斷 |   5   |
<!-- | 打包成exe     | pyinstaller    |  5   |
| 可讓使用者一鍵安裝     | NSIS    |  5   |  -->

 ### Advanced feature 35 pts.

| 實作內容 | 使用概念 | 得分 |
| -------- | -------- | :----: |
| 5個頁面(主畫面/新增/查詢/刪除/更改)     |  tlinker     | 10  |
| 能透過按鈕關閉畫面     |  tlinker     | 5   |
| 能出現訊息框提醒     |  tlinker     | 5   |
| 連接第三方資料庫    | sql,firebase   | 10|
| 使用panda Dataframe   | panda dataframe    | 5|  


### 注意事項：
* 每個畫面需有關閉畫面的功能(沒強制格式，但至少能透過程式內部關得掉)
* 若資料有輸錯或查無此人，需要有訊息框提醒。
* 完成動作也需要訊息框提醒。




## Project 繳交方式

* 創建新的repository命名為Project，然後將project整個上傳上去，有使用sql或firebase 請在demo時告知你是用哪種資料庫形式。
* 需錄製demo影片或約時間demo
* 在github上寫readme告訴我如何執行你的程式，以及你有實作的功能，語法可參考我們所有講義。
[範例專案](https://github.com/huskyncu/exercise6)
[Hackmd 語法教學](https://hackmd.io/s/quick-start-tw)
[hackmd範例](https://hackmd.io/E6gAVm9gQjK9PCsrh2T2lw?both)
* 可下載zoom來錄影後放到youtube，再把影片連結放到readmd，或你有其他方式也可以。

<!-- ## Project 參考架構(基本架構)

```python
while True:
    choice=input("(1)新增 (2) 查詢 (3)結束")
    if choice == '1':
        # 輸入使用者資料
        # 計算bmi 跟bmr 判定體位
        # 新增進資料庫
            # 如果是用dict，則名字的key可以搭配陣列的value。
            # 如果是用檔案，建議資料間要有區隔，以免讀取時出錯。
    elif choice == '2':
        # 輸入身分證字號跟名字後從資料庫裡查東西
    elif choice == '3':
        # 結束程式
        break -->





