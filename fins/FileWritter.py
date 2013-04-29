import time
import sys

class FileWritter:
    __MAX_BUFFER=0
    __iBuffCnt=0
    __sBuffer=""
    __sFileName=""

    def __init__(self,sFileName,iMaxBuffer):
        self.__MAX_BUFFER=iMaxBuffer
        self.__sFileName=sFileName

    def writeBuffered(self,sData):
        self.__iBuffCnt=self.__iBuffCnt+1
        self.__sBuffer=self.__sBuffer+sData
        if self.__iBuffCnt>=self.__MAX_BUFFER:
            self.writter(self.__sBuffer)
            self.__sBuffer=""
            self.__iBuffCnt=0
        else:
            self.__iBuffCnt=self.__iBuffCnt+1

    def writter(self,sData):
        f = open(self.__sFileName, "a")
        f.write(sData)
        f.flush()
        f.close()

    def flush(self):
        if self.__sBuffer!="":
            self.writter(self.__sBuffer)
            self.__iBuffCnt=0
            self.__sBuffer=""