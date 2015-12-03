101062206 劉子源 Assigment4


1. 有用到AppID的地方：
ask.html
result_comments.html
result.html
index.html
的下方

2. Bootstrap: 使用官網上的範例

3. 使用網路上處理 cookie的library
https://github.com/js-cookie/js-cookie

4. 
index:
需要先登入
然後最上方欄位可以回到首頁 前往問問題  得到答案頁面
按圖片的Q A 一樣可以得到結果

ask:
使用FB api
當發問成功 會顯示訊息 跟使用者說送出完成
可以按上方的按鈕直接前往result


result:
會得到使用者所問的問題
然後會依照發問時間排序
只是時間不是正確的！  但是時間是從response回傳

result_comments:
依序解析出來
然後得到所有comment