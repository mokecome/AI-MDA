# liver_medical_data_dictionary：DB data dictionary

## 1.B肝帶原

- 各字段说明

| Column Name | Description | Value Range | Value Explanation | Type |
|-------------|-------------|-------------|-------------------|------|
| 狀態 | 病人狀態 | 轉出結案,追蹤中,轉出 |  | VARCHAR(255) |
| 編號 | 病人編號 | 由1開始 | VARCHAR(255) |
| Name | 病人姓名 | | | VARCHAR(255) |
| ChartNo | 病例編號 | | | VARCHAR(255) | 
| Dr. | 醫生姓名 | 楒歆彤, 泓溫碧, 浚潔綉, 馭曦瑾, 巧琇嫻, 香靄晞, 淑翩芷, 揚墨醇, 琪翩嫣, 祐暄彤, 渝雲棻, 奕嫻淳, 瑾瑗儷, 綽卉卿, 瑜釧卿, 旻儷  涵, 巧琇嫻, 雅曦暄, 嘉勻寧, 庭雍淑, 卿凝華, 靈芷禎, 翩爽雲, 惻文涵, 承儷霓, 羽幃嫻, 奕嫻淳, 華芩儷, 晁采蓮, 逸凌雲, 儁瑾瀅, | | VARCHAR(255) | 
| F/M | 性別 | f m | f(女) m(男) | VARCHAR(255) | 
| Birthday | 生日 | | year/month/day or year/month.day | VARCHAR(255) | 
| Age | 年齡 | 年齡 | | FLOAT 
| 收案日期 | 收案日期 | | | | VARCHAR(255) |
| EchoDay | 超音波日期 | | | VARCHAR(255) |
| Dignosis | 醫師診斷 | negative, no focal lesion,lesion could not be found,no remarkable abnegative,
                no abnegative finding, no gross abnegativeities, fatty liver mild, 
                fatty liver moderate,fatty liver severe, cirrhosis,
                chronic parenchymal disease,chronic liver parenchymal disease,
                liver parenchymal disease, liver parenchyma,
                hepatitis,hepatic tumor, heaptic lesions,heaptic lesion,
                hemangioma,hepatic cysts, focal hyperplasia, 
                intraheaptic calcification, fatty metamorphosis,
                alcoholic liver disease,intrahepatic calcification,
                focal liver lesion,portal vein thrombosis, focal liver lesions,
                hepatocellular carcinoma, heterogenous fatty metamorphosis,heterogenous moderate fatty metamorphosis,
                liver heterogeneous fatty metamorphosis,
                regeneration nodules,
                regenerative nodules,liver nodules,
                hepatic nodules, hepatic tumors,
                focal hepatic lesion,focal hepatic lesions, hepatic nodule,
                hyperechoic lesion,metastatic tumor, 
                liver polycystic disease,  
                hepatic masses,hepatic mass,
                hcc,diagnostic tae,tae,
                liver biopsy | negative(陰性), no focal lesion(陰性),lesion could not be found(陰性),no remarkable abnegative(陰性),
                no abnegative finding(陰性), no gross abnegativeities(陰性),
                fatty liver mild(輕度脂肪肝), 
                fatty liver moderate(中度脂肪肝),fatty liver severe(重度脂肪肝), 
                cirrhosis(肝硬化),
                chronic parenchymal disease(肝實質病變),chronic liver parenchymal disease(肝實質病變),
                liver parenchymal disease(肝實質病變), 
                hepatitis(肝炎),hepatic tumor(肝腫瘤), hepatic tumors(肝腫瘤),
                focal hepatic lesion(局部肝臟病灶), 
                hemangioma(良性腫瘤),
                hepatic cysts(肝囊腫),
                intrahepatic calcification(肝鈣化),
                fatty metamorphosis（脂肪變性）,
                alcoholic liver disease(酒精性肝病),       
                hepatocellular carcinoma(肝細胞癌), hcc(肝細胞癌),portal vein thrombosis(門靜脈阻塞),
                heterogenous fatty metamorphosis(肝變異),heterogenous moderate fatty metamorphosis(肝變異),
                liver heterogeneous fatty metamorphosis(肝變異),
                regeneration nodules(再生性結節),focal hyperplasia(再生性結節),
                regenerative nodules(再生性結節),liver nodules(再生性結節),
                hepatic nodules(再生性結節),
                 hepatic nodule(再生性結節),
                hyperechoic lesion,metastatic tumor(癌細胞轉移), 
                liver polycystic disease(多囊肝病),  
                hepatic masses(肝腫塊),hepatic mass(肝腫塊),
                diagnostic tae(動脈血管栓塞治療術),tae(動脈血管栓塞治療術),
                liver biopsy(肝臟切片) | VARCHAR(255) |
| HBsAg | B 型肝炎表面抗原(HBsAg)「陽性」或「反應性」HBsAg 檢測結果表示此人已感染B 型肝炎病毒，可能是「急性」或「慢性」感染 | positive, negative, 缺 | positive(陽性), negative(陰性), 缺 | VARCHAR(255) |
| 檢驗日期 | 檢驗日期 | 月份 | | VARCHAR(255) |
| HBeAg | B肝e抗原(HBeAg)是pre-C/C基因的產物，當B肝病毒增殖時此種基因可以在肝細胞中發現 | positive, negative, 缺 | | VARCHAR(255) | 
| 檢驗日期.1 | HBeAg的檢驗日期 | 月份 | | VARCHAR(255) |
| GOT | GOT的值| | | FLOAT |
| 檢驗日期.2 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT | GPT的值| | | FLOAT |
| 檢驗日期.3 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| Anti-HCV | C型肝炎病毒抗體 | positive, negative, 缺 | VARCHAR(255) |
| 檢驗日期.4 | Anti-HCV檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow1 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay1 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay1 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis1 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.1 | GOT的值| | | FLOAT |
| 檢驗日期.5 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.1 | GOT的值| | | FLOAT |
| 檢驗日期.6 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow2 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay2 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay2 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis2 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.2 | GOT的值| | | FLOAT |
| 檢驗日期.7 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.2 | GPT的值| | | FLOAT |
| 檢驗日期.8 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow3 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay3 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay3 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis3 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.3 | GOT的值| | | FLOAT |
| 檢驗日期.9 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.3 | GPT的值| | | FLOAT |
| 檢驗日期.10 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow4 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay4 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay4 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis4 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.4 | GOT的值| | | FLOAT |
| 檢驗日期.11 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.4 | GPT的值| | | FLOAT |
| 檢驗日期.12 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow5 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay5 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay5 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis5 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.5 | GOT的值| | | FLOAT |
| 檢驗日期.13 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.5 | GPT的值| | | FLOAT |
| 檢驗日期.14 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow6 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay6 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay6 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis6 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.6 | GOT的值| | | FLOAT |
| 檢驗日期.15 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.6 | GPT的值| | | FLOAT |
| 檢驗日期.16 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow7 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay7 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay7 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis7 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.7 | GOT的值| | | FLOAT |
| 檢驗日期.17 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.7 | GPT的值| | | FLOAT |
| 檢驗日期.18 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow8 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay8 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay8 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis8 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.8 | GOT的值| | | FLOAT |
| 檢驗日期.19 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.8 | GPT的值| | | FLOAT |
| 檢驗日期.20 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow9 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay9 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay9 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis9 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.9 | GOT的值| | | FLOAT |
| 檢驗日期.21 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.9 | GPT的值| | | FLOAT |
| 檢驗日期.22 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow10 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay10 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay10 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis10 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.10 | GOT的值| | | FLOAT |
| 檢驗日期.23 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.10 | GPT的值| | | FLOAT |
| 檢驗日期.24 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow11 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay11 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay11 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis11 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.11 | GOT的值| | | FLOAT |
| 檢驗日期.25 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.11 | GPT的值| | | FLOAT |
| 檢驗日期.26 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow12 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay12 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay12 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis12 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.12 | GOT的值| | | FLOAT |
| 檢驗日期.27 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.12 | GPT的值| | | FLOAT |
| 檢驗日期.28 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow13 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay13 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay13 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis13 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.13 | GOT的值| | | FLOAT |
| 檢驗日期.29 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.13 | GPT的值| | | FLOAT |
| 檢驗日期.30 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow14 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay14 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay14 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis14 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.14 | GOT的值| | | FLOAT |
| 檢驗日期.31 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.14 | GPT的值| | | FLOAT |
| 檢驗日期.32 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow15 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay15 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay15 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis15 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.15 | GOT的值| | | FLOAT |
| 檢驗日期.33 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.15 | GPT的值| | | FLOAT |
| 檢驗日期.34 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow16 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay16 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay16 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis16 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.16 | GOT的值| | | FLOAT |
| 檢驗日期.35 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.16 | GPT的值| | | FLOAT |
| 檢驗日期.36 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow17 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay17 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay17 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis17 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.17 | GOT的值| | | FLOAT |
| 檢驗日期.37 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.17 | GPT的值| | | FLOAT | 
| 檢驗日期.38 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow18 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay18 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay18 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis18 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.18 | GOT的值| | | FLOAT |
| 檢驗日期.39 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.18 | GPT的值| | | FLOAT |
| 檢驗日期.40 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow19 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay19 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay19 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis19 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.19 | GOT的值| | | FLOAT |
| 檢驗日期.41 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.19 | GPT的值| | | FLOAT ||
| 檢驗日期.42 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow20 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay20 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay20 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis20 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.20 | GOT的值| | | FLOAT |
| 檢驗日期.43 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.20 | GPT的值| | | FLOAT |
| 檢驗日期.44 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow21 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay21 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay21 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis21 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.21 | GOT的值| | | FLOAT |
| 檢驗日期.45 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.21 | GPT的值| | | FLOAT |
| 檢驗日期.46 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow22 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay22 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay22 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis22 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.22 | GOT的值| | | FLOAT |
| 檢驗日期.47 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.22 | GPT的值| | | FLOAT |
| 檢驗日期.48 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow23 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) |
| OPDDay23 | 門診月份 | 月份 | |VARCHAR(255) |
| EchoDay23 | 超音波月份 | 月份 | |VARCHAR(255) |
| Dignosis23 | 醫師診斷 | 同Dignosis | 同Dignosis |VARCHAR(255) |
| GOT.23 | GOT的值| | | FLOAT |
| 檢驗日期.49 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.23 | GPT的值| | | FLOAT |
| 檢驗日期.50 | GPT的檢驗日期 | 月份 | | VARCHAR(255) | 
| real_age |實際年齡|||FLOAT|


## 2.C肝帶原

- 各字段说明

| Column Name | Description | Value Range | Value Explanation | Type |
|-------------|-------------|-------------|-------------------|------|
| 狀態 | 病人狀態 | 轉出結案,追蹤中,轉出 |  | VARCHAR(255) |
| 編號 | 病人編號 | 由1開始 | VARCHAR(255) |
| Name | 病人姓名 | | | VARCHAR(255) |
| ChartNo | 病例編號 | | | VARCHAR(255) | 
| Dr. | 醫生姓名 | 楒歆彤, 泓溫碧, 浚潔綉, 馭曦瑾, 巧琇嫻, 香靄晞, 淑翩芷, 揚墨醇, 琪翩嫣, 祐暄彤, 渝雲棻, 奕嫻淳, 瑾瑗儷, 綽卉卿, 瑜釧卿, 旻儷  涵, 巧琇嫻, 雅曦暄, 嘉勻寧, 庭雍淑, 卿凝華, 靈芷禎, 翩爽雲, 惻文涵, 承儷霓, 羽幃嫻, 奕嫻淳, 華芩儷, 晁采蓮, 逸凌雲, 儁瑾瀅, | | VARCHAR(255) | 
| F/M | 性別 | f m | f(女) m(男) | VARCHAR(255) | 
| Birthday | 生日 | | year/month/day or year/month.day | VARCHAR(255) | 
| Age | 年齡 | 年齡 | | FLOAT 
| 收案日期 | 收案日期 | | | | VARCHAR(255) |
| EchoDay | 超音波日期 | | | VARCHAR(255) |
| Dignosis | 醫師診斷 | negative, no focal lesion,lesion could not be found,no remarkable abnegative,
                no abnegative finding, no gross abnegativeities, fatty liver mild, 
                fatty liver moderate,fatty liver severe, cirrhosis,
                chronic parenchymal disease,chronic liver parenchymal disease,
                liver parenchymal disease, liver parenchyma,
                hepatitis,hepatic tumor, heaptic lesions,heaptic lesion,
                hemangioma,hepatic cysts, focal hyperplasia, 
                intraheaptic calcification, fatty metamorphosis,
                alcoholic liver disease,intrahepatic calcification,
                focal liver lesion,portal vein thrombosis, focal liver lesions,
                hepatocellular carcinoma, heterogenous fatty metamorphosis,heterogenous moderate fatty metamorphosis,
                liver heterogeneous fatty metamorphosis,
                regeneration nodules,
                regenerative nodules,liver nodules,
                hepatic nodules, hepatic tumors,
                focal hepatic lesion,focal hepatic lesions, hepatic nodule,
                hyperechoic lesion,metastatic tumor, 
                liver polycystic disease,  
                hepatic masses,hepatic mass,
                hcc,diagnostic tae,tae,
                liver biopsy | negative(陰性), no focal lesion(陰性),lesion could not be found(陰性),no remarkable abnegative(陰性),
                no abnegative finding(陰性), no gross abnegativeities(陰性),
                fatty liver mild(輕度脂肪肝), 
                fatty liver moderate(中度脂肪肝),fatty liver severe(重度脂肪肝), 
                cirrhosis(肝硬化),
                chronic parenchymal disease(肝實質病變),chronic liver parenchymal disease(肝實質病變),
                liver parenchymal disease(肝實質病變), 
                hepatitis(肝炎),hepatic tumor(肝腫瘤), hepatic tumors(肝腫瘤),
                focal hepatic lesion(局部肝臟病灶), 
                hemangioma(良性腫瘤),
                hepatic cysts(肝囊腫),
                intrahepatic calcification(肝鈣化),
                fatty metamorphosis（脂肪變性）,
                alcoholic liver disease(酒精性肝病),       
                hepatocellular carcinoma(肝細胞癌), hcc(肝細胞癌),portal vein thrombosis(門靜脈阻塞),
                heterogenous fatty metamorphosis(肝變異),heterogenous moderate fatty metamorphosis(肝變異),
                liver heterogeneous fatty metamorphosis(肝變異),
                regeneration nodules(再生性結節),focal hyperplasia(再生性結節),
                regenerative nodules(再生性結節),liver nodules(再生性結節),
                hepatic nodules(再生性結節),
                 hepatic nodule(再生性結節),
                hyperechoic lesion,metastatic tumor(癌細胞轉移), 
                liver polycystic disease(多囊肝病),  
                hepatic masses(肝腫塊),hepatic mass(肝腫塊),
                diagnostic tae(動脈血管栓塞治療術),tae(動脈血管栓塞治療術),
                liver biopsy(肝臟切片) | VARCHAR(255) |
| GOT | GOT的值| | | FLOAT |
| 檢驗日期 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT | GPT的值| | | FLOAT |
| 檢驗日期.1 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| Anti-HCV | C型肝炎病毒抗體 | positive, negative, 缺 | VARCHAR(255) |
| 檢驗日期.2 | Anti-HCV檢驗日期 | | | VARCHAR(255) |
| 6MFollow1 | 六個月後追蹤的月份 | 月份 |VARCHAR(255) |
| OPDDay1 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay1 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis1 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.1 | GOT的值| | | FLOAT | 
| 檢驗日期.3 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.1 | GPT的值 | | | FLOAT | 
| 檢驗日期.4 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow2 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay2 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay2 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis2 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.2 | GOT的值| | | FLOAT | 
| 檢驗日期.5 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.2 | GPT的值 | | | FLOAT | 
| 檢驗日期.6 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow3 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay3 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay3 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis3 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.3 | GOT的值| | | FLOAT | 
| 檢驗日期.7 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.3 | GPT的值 | | | FLOAT | 
| 檢驗日期.8 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow4 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay4 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay4 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis4 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.4 | GOT的值| | | FLOAT | 
| 檢驗日期.9 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.4 | GPT的值 | | | FLOAT | 
| 檢驗日期.10 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow5 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay5 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay5 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis5 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.5 | GOT的值| | | FLOAT | 
| 檢驗日期.11 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.5 | GPT的值 | | | FLOAT | 
| 檢驗日期.12 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow6 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay6 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay6 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis6 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.6 | GOT的值| | | FLOAT | 
| 檢驗日期.13 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.6 | GPT的值 | | | FLOAT | 
| 檢驗日期.14 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow7 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay7 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay7 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis7 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.7 | GOT的值| | | FLOAT | 
| 檢驗日期.15 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.7 | GPT的值 | | | FLOAT | 
| 檢驗日期.16 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow8 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay8 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay8 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis8 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.8 | GOT的值| | | FLOAT | 
| 檢驗日期.17 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.8 | GPT的值 | | | FLOAT | 
| 檢驗日期.18 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow9 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay9 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay9 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis9 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.9 | GOT的值| | | FLOAT | 
| 檢驗日期.19 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.9 | GPT的值 | | | FLOAT | 
| 檢驗日期.20 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow10 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay10 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay10 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis10 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.10 | GOT的值| | | FLOAT | 
| 檢驗日期.21 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.10 | GPT的值 | | | FLOAT | 
| 檢驗日期.22 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow11 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay11 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay11 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis11 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.11 | GOT的值| | | FLOAT | 
| 檢驗日期.23 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.11 | GPT的值 | | | FLOAT | 
| 檢驗日期.24 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow12 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay12 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay12 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis12 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.12 | GOT的值| | | FLOAT | 
| 檢驗日期.25 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.12 | GPT的值 | | | FLOAT | 
| 檢驗日期.26 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow13 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay13 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay13 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis13 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.13 | GOT的值| | | FLOAT | 
| 檢驗日期.27 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.13 | GPT的值 | | | FLOAT | 
| 檢驗日期.28 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow14 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay14 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay14 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis14 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.14 | GOT的值| | | FLOAT | 
| 檢驗日期.29 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.14 | GPT的值 | | | FLOAT | 
| 檢驗日期.30 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow15 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay15 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay15 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis15 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.15 | GOT的值| | | FLOAT | 
| 檢驗日期.31 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.15 | GPT的值 | | | FLOAT | 
| 檢驗日期.32 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow16 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay16 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay16 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis16 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.16 | GOT的值| | | FLOAT | 
| 檢驗日期.33 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.16 | GPT的值 | | | FLOAT | 
| 檢驗日期.34 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow17 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay17 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay17 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis17 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.17 | GOT的值| | | FLOAT | 
| 檢驗日期.35 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.17 | GPT的值 | | | FLOAT | 
| 檢驗日期.36 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow18 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay18 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay18 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis18 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.18 | GOT的值| | | FLOAT | 
| 檢驗日期.37 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.18 | GPT的值 | | | FLOAT | 
| 檢驗日期.38 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow19 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay19 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay19 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis19 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.19 | GOT的值| | | FLOAT | 
| 檢驗日期.39 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.19 | GPT的值 | | | FLOAT | 
| 檢驗日期.40 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow20 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay20 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay20 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis20 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.20 | GOT的值| | | FLOAT | 
| 檢驗日期.41 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.20 | GPT的值 | | | FLOAT | 
| 檢驗日期.42 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow21 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay21 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay21 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis21 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.21 | GOT的值| | | FLOAT | 
| 檢驗日期.43 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.21 | GPT的值 | | | FLOAT | 
| 檢驗日期.44 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow22 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay22 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay22 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis22 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.22 | GOT的值| | | FLOAT | 
| 檢驗日期.45 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.22 | GPT的值 | | | FLOAT | 
| 檢驗日期.46 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow23 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay23 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay23 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis23 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.23 | GOT的值| | | FLOAT | 
| 檢驗日期.47 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.23 | GPT的值 | | | FLOAT | 
| 檢驗日期.48 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow24 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay24 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay24 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis24 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.24 | GOT的值| | | FLOAT | 
| 檢驗日期.49 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.24 | GPT的值 | | | FLOAT | 
| 檢驗日期.50 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow25 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| real_age | 實際年齡 |||FLOAT|



## 3.bC肝帶原

- 各字段说明

| Column Name | Description | Value Range | Value Explanation | Type |
|-------------|-------------|-------------|-------------------|------|
| 狀態 | 病人狀態 | 轉出結案,追蹤中,轉出 |  | VARCHAR(255) |
| 編號 | 病人編號 | 由1開始 | VARCHAR(255) |
| Name | 病人姓名 | | | VARCHAR(255) |
| ChartNo | 病例編號 | | | VARCHAR(255) | 
| Dr. | 醫生姓名 | 楒歆彤, 泓溫碧, 浚潔綉, 馭曦瑾, 巧琇嫻, 香靄晞, 淑翩芷, 揚墨醇, 琪翩嫣, 祐暄彤, 渝雲棻, 奕嫻淳, 瑾瑗儷, 綽卉卿, 瑜釧卿, 旻儷  涵, 巧琇嫻, 雅曦暄, 嘉勻寧, 庭雍淑, 卿凝華, 靈芷禎, 翩爽雲, 惻文涵, 承儷霓, 羽幃嫻, 奕嫻淳, 華芩儷, 晁采蓮, 逸凌雲, 儁瑾瀅, | | VARCHAR(255) | 
| F/M | 性別 | f m | f(女) m(男) | VARCHAR(255) | 
| Birthday | 生日 | | year/month/day or year/month.day | VARCHAR(255) | 
| Age | 年齡 | 年齡 | | FLOAT 
| 收案日期 | 收案日期 | | | | VARCHAR(255) |
| EchoDay | 超音波日期 | | | VARCHAR(255) |
| Dignosis | 醫師診斷 | negative, no focal lesion,lesion could not be found,no remarkable abnegative,
                no abnegative finding, no gross abnegativeities, fatty liver mild, 
                fatty liver moderate,fatty liver severe, cirrhosis,
                chronic parenchymal disease,chronic liver parenchymal disease,
                liver parenchymal disease, liver parenchyma,
                hepatitis,hepatic tumor, heaptic lesions,heaptic lesion,
                hemangioma,hepatic cysts, focal hyperplasia, 
                intraheaptic calcification, fatty metamorphosis,
                alcoholic liver disease,intrahepatic calcification,
                focal liver lesion,portal vein thrombosis, focal liver lesions,
                hepatocellular carcinoma, heterogenous fatty metamorphosis,heterogenous moderate fatty metamorphosis,
                liver heterogeneous fatty metamorphosis,
                regeneration nodules,
                regenerative nodules,liver nodules,
                hepatic nodules, hepatic tumors,
                focal hepatic lesion,focal hepatic lesions, hepatic nodule,
                hyperechoic lesion,metastatic tumor, 
                liver polycystic disease,  
                hepatic masses,hepatic mass,
                hcc,diagnostic tae,tae,
                liver biopsy | negative(陰性), no focal lesion(陰性),lesion could not be found(陰性),no remarkable abnegative(陰性),
                no abnegative finding(陰性), no gross abnegativeities(陰性),
                fatty liver mild(輕度脂肪肝), 
                fatty liver moderate(中度脂肪肝),fatty liver severe(重度脂肪肝), 
                cirrhosis(肝硬化),
                chronic parenchymal disease(肝實質病變),chronic liver parenchymal disease(肝實質病變),
                liver parenchymal disease(肝實質病變), 
                hepatitis(肝炎),hepatic tumor(肝腫瘤), hepatic tumors(肝腫瘤),
                focal hepatic lesion(局部肝臟病灶), 
                hemangioma(良性腫瘤),
                hepatic cysts(肝囊腫),
                intrahepatic calcification(肝鈣化),
                fatty metamorphosis（脂肪變性）,
                alcoholic liver disease(酒精性肝病),       
                hepatocellular carcinoma(肝細胞癌), hcc(肝細胞癌),portal vein thrombosis(門靜脈阻塞),
                heterogenous fatty metamorphosis(肝變異),heterogenous moderate fatty metamorphosis(肝變異),
                liver heterogeneous fatty metamorphosis(肝變異),
                regeneration nodules(再生性結節),focal hyperplasia(再生性結節),
                regenerative nodules(再生性結節),liver nodules(再生性結節),
                hepatic nodules(再生性結節),
                 hepatic nodule(再生性結節),
                hyperechoic lesion,metastatic tumor(癌細胞轉移), 
                liver polycystic disease(多囊肝病),  
                hepatic masses(肝腫塊),hepatic mass(肝腫塊),
                diagnostic tae(動脈血管栓塞治療術),tae(動脈血管栓塞治療術),
                liver biopsy(肝臟切片) | VARCHAR(255) |
| HBsAg | B 型肝炎表面抗原(HBsAg)「陽性」或「反應性」HBsAg 檢測結果表示此人已感染B 型肝炎病毒，可能是「急性」或「慢性」感染 | positive, negative, 缺 | positive(陽性), negative(陰性), 缺 | VARCHAR(255) |
| 檢驗日期 | 檢驗日期 | | | VARCHAR(255) |
| HBeAg | B肝e抗原(HBeAg)是pre-C/C基因的產物，當B肝病毒增殖時此種基因可以在肝細胞中發現 | positive, negative, 缺 | | VARCHAR(255) | 
| 檢驗日期.1 | HBeAg的檢驗日期 | | | VARCHAR(255) |
| GOT | GOT的全名為天門冬胺酸轉胺酶（Glutamic Oxaloacetic Transaminase，又稱ASpartate aminoTransferase（AST）| | | FLOAT |
| 檢驗日期.2 | GOT的檢驗日期 | | | VARCHAR(255) |
| GPT | GPT的全名為丙胺酸轉胺酶（Glutamic Pyruvic Transaminase），又稱ALanine aminoTransferase（ALT）| | | FLOAT |
| 檢驗日期.3 | GPT的檢驗日期 | | | VARCHAR(255) |
| Anti-HCV | C型肝炎病毒抗體 | positive, negative, 缺 | VARCHAR(255) |
| 檢驗日期.4 | Anti-HCV檢驗日期 | | | VARCHAR(255) |
| 6MFollow1 | 六個月後追蹤的月份 | 月份 |VARCHAR(255) |
| OPDDay1 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay1 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis1 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.1 | GOT的值| | | FLOAT | 
| 檢驗日期.5 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.1 | GPT的值 | | | FLOAT | 
| 檢驗日期.6 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow2 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay2 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay2 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis2 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.2 | GOT的值| | | FLOAT | 
| 檢驗日期.7 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.2 | GPT的值 | | | FLOAT | 
| 檢驗日期.8 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow3 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay3 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay3 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis3 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.3 | GOT的值| | | FLOAT | 
| 檢驗日期.9 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.3 | GPT的值 | | | FLOAT | 
| 檢驗日期.10 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow4 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay4 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay4 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis4 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.4 | GOT的值| | | FLOAT | 
| 檢驗日期.11 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.4 | GPT的值 | | | FLOAT | 
| 檢驗日期.12 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow5 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay5 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay5 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis5 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.5 | GOT的值| | | FLOAT | 
| 檢驗日期.13 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.5 | GPT的值 | | | FLOAT | 
| 檢驗日期.14 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow6 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay6 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay6 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis6 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.6 | GOT的值| | | FLOAT | 
| 檢驗日期.15 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.6 | GPT的值 | | | FLOAT | 
| 檢驗日期.16 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow7 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay7 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay7 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis7 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.7 | GOT的值| | | FLOAT | 
| 檢驗日期.17 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.7 | GPT的值 | | | FLOAT | 
| 檢驗日期.18 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow8 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay8 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay8 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis8 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.8 | GOT的值| | | FLOAT | 
| 檢驗日期.19 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.8 | GPT的值 | | | FLOAT | 
| 檢驗日期.20 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow9 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay9 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay9 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis9 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.9 | GOT的值| | | FLOAT | 
| 檢驗日期.21 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.9 | GPT的值 | | | FLOAT | 
| 檢驗日期.22 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow10 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| OPDDay10 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay10 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis10 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.10 | GOT的值| | | FLOAT | 
| 檢驗日期.23 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.10 | GPT的值 | | | FLOAT | 
| 檢驗日期.24 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| OPDDay11 | 門診月份 | 月份 | | VARCHAR(255) | 
| EchoDay11 | 超音波月份 | 月份 | |VARCHAR(255) | 
| Dignosis11 | 醫師診斷 | 同Dignosis | 同Dignosis | VARCHAR(255) | 
| GOT.11 | GOT的值| | | FLOAT | 
| 檢驗日期.25 | GOT的檢驗日期 | 月份 | | VARCHAR(255) |
| GPT.11 | GPT的值 | | | FLOAT | 
| 檢驗日期.26 | GPT的檢驗日期 | 月份 | | VARCHAR(255) |
| 6mfollow11 | 六個月後追蹤的月份 | 月份 | | VARCHAR(255) | 
| real_age | 實際年齡 |||FLOAT|
  
