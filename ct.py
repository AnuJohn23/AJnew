# -*- coding: utf-8 -*-
import cv2
import tensorflow as tf
import numpy as np
import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Path to label map file
PATH_TO_LABELS = os.path.join('labelmap.txt')

# Load the label map
with open(PATH_TO_LABELS, 'r') as f:
    labels = [line.strip() for line in f.readlines()]

if labels[0] == '???':
    del(labels[0])

# Load the model
interpreter = tf.lite.Interpreter(model_path="detect.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

b=0

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("finalui.ui",self)
        
        
        self.start.clicked.connect(self.starter)
        self.resultButton.clicked.connect(self.resultprint)
        self.printing
        

    def starter(self):
        print("ijdjojh")
        cap = cv2.VideoCapture(0)
        
        wine_glasscount=0
        bowlcount=0
        spooncount=0
        knifecount=0
        forkcount=0
        scissorscount=0
        bottlecount=0
        
        wine_glasscounter=0
        bowlcounter=0
        spooncounter=0
        knifecounter=0
        forkcounter=0
        scissorscounter=0
        bottlecounter=0
        
        botlep=0
        scissorsp=0
        forkp=0
        knifep=0
        spoonp=0
        bowlp=0
        wine_glassp=0
        
        while True:
            # Capture image
            ret, img_org = cap.read()
            key = cv2.waitKey(1)
            if key == 27:  # ESC
                break
        
            # Prepare input image
            img = cv2.cvtColor(img_org, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (300, 300))
            img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2])  # (1, 300, 300, 3)
            img = img.astype(np.uint8)
        
            # Set input tensor
            interpreter.set_tensor(input_details[0]['index'], img)
        
            # Run inference
            interpreter.invoke()
        
            # Get output tensors
            boxes = interpreter.get_tensor(output_details[0]['index'])
            classes = interpreter.get_tensor(output_details[1]['index'])
            scores = interpreter.get_tensor(output_details[2]['index'])
            num = interpreter.get_tensor(output_details[3]['index'])
        
            wine_glasscount=0
            bowlcount=0
            spooncount=0
            knifecount=0
            forkcount=0
            scissorscount=0
            bottlecount=0
            
            addval=0
            
            for i in range(boxes.shape[1]):
                if scores[0, i] > 0.5:
                    box = boxes[0, i, :]
                    x0 = int(box[1] * img_org.shape[1])
                    y0 = int(box[0] * img_org.shape[0])
                    x1 = int(box[3] * img_org.shape[1])
                    y1 = int(box[2] * img_org.shape[0])
                    box = box.astype(np.int)
                    cv2.rectangle(img_org, (x0, y0), (x1, y1), (255, 0, 0), 2)
                    cv2.rectangle(img_org, (x0, y0), (x0 + 100, y0 - 30), (255, 0, 0), -1)
                    object_name = labels[int(classes[0, i])]
                    cv2.putText(img_org, object_name, (x0, y0), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    print(object_name)
                    
                    self.nameBox.setText(object_name)
    
                    #Row count
                    self.tableWidget.setRowCount(7) 
                  
                    #Column count
                    self.tableWidget.setColumnCount(3)
                    
                    self.tableWidget.setItem(0,0, QTableWidgetItem("Name"))
                    self.tableWidget.setItem(0,1, QTableWidgetItem("qty"))
                    self.tableWidget.setItem(0,2, QTableWidgetItem("price"))
                    
                    if object_name == "bottle":
                        bottlecount += 1 
                        bottlecounter += 1
                        if bottlecounter>10:
                            
                            self.tableWidget.setItem(1,0, QTableWidgetItem("bottle"))
                            botlep=(bottlecount*5)
                            bottlecnt=str(bottlecount)
                            bottleprice=str(botlep)
                            self.tableWidget.setItem(1,1, QTableWidgetItem(bottlecnt))
                            self.tableWidget.setItem(1,2, QTableWidgetItem(bottleprice))
                            
                    if object_name == "scissors":
                        scissorscount += 1  
                        scissorscounter += 1
                        if scissorscounter>=10:
                            self.tableWidget.setItem(2,0, QTableWidgetItem("scissors"))
                            scissorsp=(scissorscount*15)
                            scissorscnt=str(scissorscount)
                            scissorsprice=str(scissorsp)
                            self.tableWidget.setItem(2,1, QTableWidgetItem(scissorscnt))
                            self.tableWidget.setItem(2,2, QTableWidgetItem(scissorsprice))
                    if object_name == "fork":
                        forkcount += 1 
                        forkcounter += 1
                        if forkcounter>=10:                            
                            self.tableWidget.setItem(3,0, QTableWidgetItem("fork"))
                            forkp=(forkcount*12)
                            forkcnt=str(forkcount)
                            forkprice=str(forkp)                            
                            self.tableWidget.setItem(3,1, QTableWidgetItem(forkcnt))
                            self.tableWidget.setItem(3,2, QTableWidgetItem(forkprice))
                    if object_name == "knife":
                        knifecount += 1
                        knifecounter += 1
                        if knifecounter >= 10:                            
                            self.tableWidget.setItem(4,0, QTableWidgetItem("knife"))
                            knifep=(knifecount*35)
                            knifecnt=str(knifecount)
                            knifeprice=str(knifep)
                            self.tableWidget.setItem(4,1, QTableWidgetItem(knifecnt))
                            self.tableWidget.setItem(4,2, QTableWidgetItem(knifeprice))
                    if object_name == "spoon":
                        spooncount += 1    
                        spooncounter += 1
                        if spooncounter >= 10:        
                            self.tableWidget.setItem(5,0, QTableWidgetItem("spoon"))
                            spoonp=(spooncount*18)
                            spooncnt=str(spooncount)
                            spoonprice=str(spoonp)
                            self.tableWidget.setItem(5,1, QTableWidgetItem(spooncnt))
                            self.tableWidget.setItem(5,2, QTableWidgetItem(spoonprice))
                    if object_name == "bowl":
                        bowlcount += 1  
                        bowlcounter += 1
                        if bowlcounter >= 10:                          
                            self.tableWidget.setItem(6,0, QTableWidgetItem("bowl"))
                            bowlp=(bowlcount*56)
                            bowlcnt=str(bowlcount)
                            bowlprice=str(bowlp)
                            self.tableWidget.setItem(6,1, QTableWidgetItem(bowlcnt))
                            self.tableWidget.setItem(6,2, QTableWidgetItem(bowlprice))
                    if object_name == "wine glass":
                        wine_glasscount += 1
                        wine_glasscounter += 1
                        if wine_glasscounter >= 10:                          
                            self.tableWidget.setItem(7,0, QTableWidgetItem("wine glass"))
                            wine_glassp=(wine_glasscount*78)
                            wine_glasscnt=str(wine_glasscount)
                            wine_glassprice=str(wine_glassp)
                            self.tableWidget.setItem(7,1, QTableWidgetItem(wine_glasscnt))
                            self.tableWidget.setItem(7,2, QTableWidgetItem(wine_glassprice))
                                   
                    
                    addval=(botlep+scissorsp+forkp+knifep+spoonp+bowlp+wine_glassp)
                    
                    self.printing =addval                
        
            cv2.imshow('image', img_org)
            ConvertToQtFormat = QImage(img_org.data, img_org.shape[1], img_org.shape[0], QImage.Format_RGB888).rgbSwapped()
            Pic = ConvertToQtFormat.scaled(371, 311, Qt.KeepAspectRatio)
            self.label.setPixmap(QPixmap.fromImage(Pic))
        
        cap.release()
        cv2.destroyAllWindows()
        
    def resultprint(self):
        
        b=self.printing
        # s=float(a)
        # b=round(s, 2) 
        b=str(b)
        self.finalResult.setText(b)
        
        img = cv2.imread("pay.jpg")
        cv2.imshow("qr_code", img)
        cv2.waitKey(0)
        
app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(869)
widget.setFixedHeight(580)
widget.show()
sys.exit(app.exec_())        