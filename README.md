# affiliateItemsClassifer

Sample project based on [scikit-learn text tutorial](http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html) for identifying product from affilate marketing catalog.

## Install
```bash
pip install scipy numpy scikit-learn
```

## Goal
The goal of this machine learning scripts is to predict to which product an affiliate items refer.

## Sample training data
Training data are in file data/products_items.json.

```json
{"PRD_ID": 533,"ITM_ID": 529356,"ITM_TITLE": "PNEU Pirelli ANGEL ST 120/60R17 55W TL,Avant","PRD_NAME": "Pirelli Angel ST"}
```

 * PRD_ID = Product ID. This is the category in the classification algorithm.
 * ITM_ID = Affiliate's item ID
 * ITM_TITLE = Item title provided by affiliate marketing feed. We use this data as based text document for learning
 * PRD_NAME = Product name. This is the category label.

In the previous row, item "PNEU Pirelli ANGEL ST 120/60R17 55W TL,Avant" refer to the product "Pirelli Angel ST" (A motorcycle tyre). 

This item title is a concatened string of : 
 * "Pneu" french translation of "tyre"
 * "Pirelli" Product brand
 * "ANGEL ST" Product name
 * "120/60R17 55W TL" Tyre dimension
 * "Avant" french translation of "Front" (Motorcycle's tyres are different at front and rear)

## Sample run
Output display success rate (comparing predicted data and training data) and 10 predicted results

```bash
python classifier.py
Success rate: 0.914490527394
Item "Pneu Moto RACETEC SLICK REAR : Pneus moto compétition 190/60 -17 K2 NHS" classified as product "Metzeler Racetec"
Item "Pneu Moto DIABLO ROSSO 2 : Pneus moto sport 180/55 R17 TL 73 W" classified as product "Pirelli Diablo Rosso 2"
Item "Pneu Moto PILOT POWER REAR : Pneus moto route 180/55 R17 TL 73 W B" classified as product "Michelin Pilot Power"
Item "Dunlop Sportmax Qualifier NK 200/50 ZR17 TL (75W) M/C, roue arrière" classified as product "Dunlop Qualifier"
Item "Metzeler Racetec SM Front K1 125/80 R420 TL NHS" classified as product "Metzeler Racetec"
Item "PNEU Dunlop SPORTMAX ROADSMART 170/60R17 72W TL,Arrière" classified as product "Dunlop Roadsmart"
Item "PNEU Bridgestone BATTLAX BT-016 190/55R17 75W TL,arrière" classified as product "Bridgestone BT 016"
Item "Pneu Moto BATTLAX BT 016 PRO REAR : Pneus moto sport 190/55 -17 75 W" classified as product "Bridgestone BT 016"
Item "Michelin PILOT ROAD 2 FRONT 120/70 ZR18 TL 59(W) M/C" classified as product "Michelin Pilot Road 3"
Item "Metzeler Racetec Rain K1 Block 160/60 R17 TL NHS" classified as product "Metzeler Racetec"
```
## About me
http://petitchevalroux.net