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
                no abnegative finding, no gross abnegativeities,
                fatty liver mild, 
                fatty liver moderate,fatty liver severe, moderate fatty liver,
                fatty liver, cirrhosis,liver cirrosis,liver cirrhosis, liver criihosis,
                chronic parenchymal disease,chronic liver parenchymal disease,
                liver parenchymal disease, liver parenchyma,
                hepatitis,hepatic cyst,hepatic tumor, heaptic lesions,heaptic lesion,
                hemangioma,hemangiomas,cyst, liver cysts, cysts, hepaticcysts, hepatic cysts,
                intrahepatic calfication,focal hyperplasia, 
                intraheaptic calcification,intrahepatic calcifications, intrahepatic calcificiation,
                fatty metamorphosis,
                alcoholic liver disease,intrahepatic calcification,
                focal liver lesion,portal vein thrombosis, focal liver lesions,
                hepatocellular carcinoma,
                heterogenous fatty metamorphosis(肝變異),heterogenous moderate fatty metamorphosis,
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
                fatty liver moderate(中度脂肪肝),fatty liver severe(重度脂肪肝), moderate fatty liver(中度脂肪肝),
                fatty liver(輕度脂肪肝), cirrhosis(肝硬化),liver cirrosis(肝硬化),liver cirrhosis(肝硬化), liver criihosis(肝硬化),
                chronic parenchymal disease(肝實質病變),chronic liver parenchymal disease(肝實質病變),
                liver parenchymal disease(肝實質病變), liver parenchyma(肝實質病變),
                hepatitis(肝炎),hepatic cyst(肝囊腫),hepatic tumor(肝腫瘤), hepatic tumors(肝腫瘤),
                heaptic lesions(局部肝臟病灶),heaptic lesion(局部肝臟病灶),focal hepatic lesion(局部肝臟病灶),
                hemangioma(良性腫瘤),hemangiomas(良性腫瘤),cyst, liver cysts(肝囊腫), cysts(肝囊腫), hepaticcysts(肝囊腫), 
                hepatic cysts(肝囊腫),
                intrahepatic calfication(肝鈣化), 
                intraheaptic calcification(肝鈣化),intrahepatic calcifications(肝鈣化), intrahepatic calcificiation(肝鈣化),
                fatty metamorphosis（脂肪變性）,
                alcoholic liver disease(酒精性肝病),intrahepatic calcification(肝鈣化),
                focal liver lesion(局部肝臟病灶), focal liver lesions(局部肝臟病灶),
                hepatocellular carcinoma(肝細胞癌), hcc(肝細胞癌),portal vein thrombosis(門靜脈阻塞),
                heterogenous fatty metamorphosis(肝變異),heterogenous moderate fatty metamorphosis(肝變異),
                liver heterogeneous fatty metamorphosis(肝變異),
                regeneration nodules(再生性結節),focal hyperplasia(再生性結節),
                regenerative nodules(再生性結節),liver nodules(再生性結節),
                hepatic nodules(再生性結節),
                focal hepatic lesions(局部肝臟病灶), hepatic nodule(再生性結節),
                hyperechoic lesion,metastatic tumor(癌細胞轉移), 
                liver polycystic disease(多囊肝病),  
                hepatic masses(肝腫塊),hepatic mass(肝腫塊),
                diagnostic tae(動脈血管栓塞治療術),tae(動脈血管栓塞治療術),
                liver biopsy(肝臟切片) | VARCHAR(255) |
| HBsAg | B 型肝炎表面抗原(HBsAg)「陽性」或「反應性」HBsAg 檢測結果表示此人已感染B 型肝炎病毒，可能是「急性」或「慢性」感染 | positive, negative, 缺 | positive(陽性), negative(陰性), 缺
| 檢驗日期 | 檢驗日期 | | | VARCHAR(255) |
| HBeAg | B肝e抗原(HBeAg)是pre-C/C基因的產物，當B肝病毒增殖時此種基因可以在肝細胞中發現 | positive, negative, 缺 | | VARCHAR(255) | 
| 檢驗日期.1 | HBeAg的檢驗日期 | | | VARCHAR(255) |
| GOT | GOT的全名為天門冬胺酸轉胺酶（Glutamic Oxaloacetic Transaminase，又稱ASpartate aminoTransferase（AST）| | | FLOAT |
| 檢驗日期.2 | GOT的檢驗日期 | | | VARCHAR(255) |
| GPT | GPT的全名為丙胺酸轉胺酶（Glutamic Pyruvic Transaminase），又稱ALanine aminoTransferase（ALT）| | | FLOAT |
| 檢驗日期.3 | GPT的檢驗日期 | | | VARCHAR(255) |
| Anti-HCV | C型肝炎病毒抗體 | positive, negative, 缺 | VARCHAR(255) |
| 檢驗日期.4 | Anti-HCV檢驗日期 | | | VARCHAR(255) |
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
                no abnegative finding, no gross abnegativeities,
                fatty liver mild, 
                fatty liver moderate,fatty liver severe, moderate fatty liver,
                fatty liver, cirrhosis,liver cirrosis,liver cirrhosis, liver criihosis,
                chronic parenchymal disease,chronic liver parenchymal disease,
                liver parenchymal disease, liver parenchyma,
                hepatitis,hepatic cyst,hepatic tumor, heaptic lesions,heaptic lesion,
                hemangioma,hemangiomas,cyst, liver cysts, cysts, hepaticcysts, hepatic cysts,
                intrahepatic calfication,focal hyperplasia, 
                intraheaptic calcification,intrahepatic calcifications, intrahepatic calcificiation,
                fatty metamorphosis,
                alcoholic liver disease,intrahepatic calcification,
                focal liver lesion,portal vein thrombosis, focal liver lesions,
                hepatocellular carcinoma,
                heterogenous fatty metamorphosis(肝變異),heterogenous moderate fatty metamorphosis,
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
                fatty liver moderate(中度脂肪肝),fatty liver severe(重度脂肪肝), moderate fatty liver(中度脂肪肝),
                fatty liver(輕度脂肪肝), cirrhosis(肝硬化),liver cirrosis(肝硬化),liver cirrhosis(肝硬化), liver criihosis(肝硬化),
                chronic parenchymal disease(肝實質病變),chronic liver parenchymal disease(肝實質病變),
                liver parenchymal disease(肝實質病變), liver parenchyma(肝實質病變),
                hepatitis(肝炎),hepatic cyst(肝囊腫),hepatic tumor(肝腫瘤), hepatic tumors(肝腫瘤),
                heaptic lesions(局部肝臟病灶),heaptic lesion(局部肝臟病灶),focal hepatic lesion(局部肝臟病灶),
                hemangioma(良性腫瘤),hemangiomas(良性腫瘤),cyst, liver cysts(肝囊腫), cysts(肝囊腫), hepaticcysts(肝囊腫), 
                hepatic cysts(肝囊腫),
                intrahepatic calfication(肝鈣化), 
                intraheaptic calcification(肝鈣化),intrahepatic calcifications(肝鈣化), intrahepatic calcificiation(肝鈣化),
                fatty metamorphosis（脂肪變性）,
                alcoholic liver disease(酒精性肝病),intrahepatic calcification(肝鈣化),
                focal liver lesion(局部肝臟病灶), focal liver lesions(局部肝臟病灶),
                hepatocellular carcinoma(肝細胞癌), hcc(肝細胞癌),portal vein thrombosis(門靜脈阻塞),
                heterogenous fatty metamorphosis(肝變異),heterogenous moderate fatty metamorphosis(肝變異),
                liver heterogeneous fatty metamorphosis(肝變異),
                regeneration nodules(再生性結節),focal hyperplasia(再生性結節),
                regenerative nodules(再生性結節),liver nodules(再生性結節),
                hepatic nodules(再生性結節),
                focal hepatic lesions(局部肝臟病灶), hepatic nodule(再生性結節),
                hyperechoic lesion,metastatic tumor(癌細胞轉移), 
                liver polycystic disease(多囊肝病),  
                hepatic masses(肝腫塊),hepatic mass(肝腫塊),
                diagnostic tae(動脈血管栓塞治療術),tae(動脈血管栓塞治療術),
                liver biopsy(肝臟切片) | VARCHAR(255) |
| HBsAg | B 型肝炎表面抗原(HBsAg)「陽性」或「反應性」HBsAg 檢測結果表示此人已感染B 型肝炎病毒，可能是「急性」或「慢性」感染 | positive, negative, 缺 | positive(陽性), negative(陰性), 缺
| 檢驗日期 | 檢驗日期 | | | VARCHAR(255) |
| HBeAg | B肝e抗原(HBeAg)是pre-C/C基因的產物，當B肝病毒增殖時此種基因可以在肝細胞中發現 | positive, negative, 缺 | | VARCHAR(255) | 
| 檢驗日期.1 | HBeAg的檢驗日期 | | | VARCHAR(255) |
| GOT | GOT的全名為天門冬胺酸轉胺酶（Glutamic Oxaloacetic Transaminase，又稱ASpartate aminoTransferase（AST）| | | FLOAT |
| 檢驗日期.2 | GOT的檢驗日期 | | | VARCHAR(255) |
| GPT | GPT的全名為丙胺酸轉胺酶（Glutamic Pyruvic Transaminase），又稱ALanine aminoTransferase（ALT）| | | FLOAT |
| 檢驗日期.3 | GPT的檢驗日期 | | | VARCHAR(255) |
| Anti-HCV | C型肝炎病毒抗體 | positive, negative, 缺 | VARCHAR(255) |
| 檢驗日期.4 | Anti-HCV檢驗日期 | | | VARCHAR(255) |
| 6MFollow1 | 六個月後追蹤的月份與註記 | 月份與一些註記 |VARCHAR(255) |
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
                no abnegative finding, no gross abnegativeities,
                fatty liver mild, 
                fatty liver moderate,fatty liver severe, moderate fatty liver,
                fatty liver, cirrhosis,liver cirrosis,liver cirrhosis, liver criihosis,
                chronic parenchymal disease,chronic liver parenchymal disease,
                liver parenchymal disease, liver parenchyma,
                hepatitis,hepatic cyst,hepatic tumor, heaptic lesions,heaptic lesion,
                hemangioma,hemangiomas,cyst, liver cysts, cysts, hepaticcysts, hepatic cysts,
                intrahepatic calfication,focal hyperplasia, 
                intraheaptic calcification,intrahepatic calcifications, intrahepatic calcificiation,
                fatty metamorphosis,
                alcoholic liver disease,intrahepatic calcification,
                focal liver lesion,portal vein thrombosis, focal liver lesions,
                hepatocellular carcinoma,
                heterogenous fatty metamorphosis(肝變異),heterogenous moderate fatty metamorphosis,
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
                fatty liver moderate(中度脂肪肝),fatty liver severe(重度脂肪肝), moderate fatty liver(中度脂肪肝),
                fatty liver(輕度脂肪肝), cirrhosis(肝硬化),liver cirrosis(肝硬化),liver cirrhosis(肝硬化), liver criihosis(肝硬化),
                chronic parenchymal disease(肝實質病變),chronic liver parenchymal disease(肝實質病變),
                liver parenchymal disease(肝實質病變), liver parenchyma(肝實質病變),
                hepatitis(肝炎),hepatic cyst(肝囊腫),hepatic tumor(肝腫瘤), hepatic tumors(肝腫瘤),
                heaptic lesions(局部肝臟病灶),heaptic lesion(局部肝臟病灶),focal hepatic lesion(局部肝臟病灶),
                hemangioma(良性腫瘤),hemangiomas(良性腫瘤),cyst, liver cysts(肝囊腫), cysts(肝囊腫), hepaticcysts(肝囊腫), 
                hepatic cysts(肝囊腫),
                intrahepatic calfication(肝鈣化), 
                intraheaptic calcification(肝鈣化),intrahepatic calcifications(肝鈣化), intrahepatic calcificiation(肝鈣化),
                fatty metamorphosis（脂肪變性）,
                alcoholic liver disease(酒精性肝病),intrahepatic calcification(肝鈣化),
                focal liver lesion(局部肝臟病灶), focal liver lesions(局部肝臟病灶),
                hepatocellular carcinoma(肝細胞癌), hcc(肝細胞癌),portal vein thrombosis(門靜脈阻塞),
                heterogenous fatty metamorphosis(肝變異),heterogenous moderate fatty metamorphosis(肝變異),
                liver heterogeneous fatty metamorphosis(肝變異),
                regeneration nodules(再生性結節),focal hyperplasia(再生性結節),
                regenerative nodules(再生性結節),liver nodules(再生性結節),
                hepatic nodules(再生性結節),
                focal hepatic lesions(局部肝臟病灶), hepatic nodule(再生性結節),
                hyperechoic lesion,metastatic tumor(癌細胞轉移), 
                liver polycystic disease(多囊肝病),  
                hepatic masses(肝腫塊),hepatic mass(肝腫塊),
                diagnostic tae(動脈血管栓塞治療術),tae(動脈血管栓塞治療術),
                liver biopsy(肝臟切片) | VARCHAR(255) |
| HBsAg | B 型肝炎表面抗原(HBsAg)「陽性」或「反應性」HBsAg 檢測結果表示此人已感染B 型肝炎病毒，可能是「急性」或「慢性」感染 | positive, negative, 缺 | positive(陽性), negative(陰性), 缺
| 檢驗日期 | 檢驗日期 | | | VARCHAR(255) |
| HBeAg | B肝e抗原(HBeAg)是pre-C/C基因的產物，當B肝病毒增殖時此種基因可以在肝細胞中發現 | positive, negative, 缺 | | VARCHAR(255) | 
| 檢驗日期.1 | HBeAg的檢驗日期 | | | VARCHAR(255) |
| GOT | GOT的全名為天門冬胺酸轉胺酶（Glutamic Oxaloacetic Transaminase，又稱ASpartate aminoTransferase（AST）| | | FLOAT |
| 檢驗日期.2 | GOT的檢驗日期 | | | VARCHAR(255) |
| GPT | GPT的全名為丙胺酸轉胺酶（Glutamic Pyruvic Transaminase），又稱ALanine aminoTransferase（ALT）| | | FLOAT |
| 檢驗日期.3 | GPT的檢驗日期 | | | VARCHAR(255) |
| Anti-HCV | C型肝炎病毒抗體 | positive, negative, 缺 | VARCHAR(255) |
| 檢驗日期.4 | Anti-HCV檢驗日期 | | | VARCHAR(255) |
| 6MFollow1 | 六個月後追蹤的月份與註記 | 月份與一些註記 |VARCHAR(255) |
| real_age | 實際年齡 |||FLOAT|
  
