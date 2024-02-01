圖型降低雜訊
為一個盡可能保持圖型細節和結構資訊時去儲訓的過程
在Python中採用 Rudin-Osher-Fatemide-noising(ROF)模型

-----------------------------------------
1-9-1_Simulation
功能：模擬實現降低雜訊處裡
自行繪製並使用高斯模糊和ROF降低雜訊

-----------------------------------------
1-9-2_Reality
功能：真實圖型實現降低雜訊處裡
提供影像並使用高斯模糊和ROF降低雜訊

-----------------------------------------
1-9-3_Add Noise and Reduce
功能：增加雜訊和實現降低雜訊的處理
1.椒鹽雜訊(salt & pepper noise)
=>隨機在影像上產生黑色和白色的像素
https://openhome.cc/Gossip/DCHardWay/ImageNoise.html

2.高斯雜訊(Additive white Gaussiaan noise,， AWGN)
=>通訊領域中指的是一種功率譜函數是常數(白色雜訊)
https://jason-chen-1992.weebly.com/home/-noise-and-filter