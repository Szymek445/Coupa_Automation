from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
import getpass
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from tkinter import filedialog
import os


messagebox.showwarning("Closing Chrome", "Your Chrome app is going to be closed automatically after you click 'ok'")

try:
    os.system("TASKKILL /F /IM chrome.exe")
except:
    pass


def resource_path(relative_path: str) -> str:

    base_path = os.path.dirname(__file__)
    
    return os.path.join(base_path, relative_path)

user_name = getpass.getuser()
no_invoice = []
no_attachment = []
doubles = []
errors = []
CHROME_DRIVER_PATH = './driver/chromedriver.exe'

class Program:

    def __init__(self, direct):
        self.direct = direct
        self.webdriver = webdriver
        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir=C:\\Users\\{user_name}\\AppData\\Local\\Google\\Chrome\\User Data")
        self.direct = self.direct.replace(r"/", "\\")
        p = {"download.default_directory": str(self.direct)}
        options.add_experimental_option("prefs", p)
        self.driver = self.webdriver.Chrome(executable_path=resource_path(CHROME_DRIVER_PATH),chrome_options=options)

    def get_site(self, choise):
        url1 = "https://YOUR.coupahost.com/invoices"
        url2 = "https://YOUR.coupahost.com/invoices"

        if choise == 1:
            self.driver.get(url1)

        if choise == 2:
            self.driver.get(url2)



    def advance_search(self, nr):
        time.sleep(0.5)

        try:
            fild_inv = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[1]/div[3]/div/section/form/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/span[2]/span/input'))
            fild_inv.send_keys("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")
            time.sleep(0.5)
            fild_inv.send_keys(nr)
        except:
            advancedSearchElement = WebDriverWait(self.driver, 40).until(lambda driver: self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[1]/div[3]/div/section/form/div[1]/div[1]/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[6]/a/span'))
            advancedSearchElement.click()

            fild_inv = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[1]/div[3]/div/section/form/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/span[2]/span/input'))
            fild_inv.send_keys("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")
            time.sleep(0.5)
            fild_inv.send_keys(nr) 


    def search(self):
        try:
            sercz = WebDriverWait(self.driver, 5).until(lambda driver: self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[1]/div[3]/div/section/form/div[1]/div[1]/div[2]/div[2]/div/button/span'))
            sercz.click()
            time.sleep(2)
        
        except:
            print("Fatal error")

    def name_FV(self, nr):
        try:
            nr = nr.replace(r"/", " ")
        except:
            pass
        try:
            nr = nr.replace(r":", " ")
        except:
            pass    
        try:    
            nr = nr.replace(r"*", " ")
        except:
            pass    
        try:    
            nr = nr.replace(r"?", " ")
        except:
            pass
        try:
            nr = nr.replace(r'"', " ")
        except:
            pass    
        try:    
            nr = nr.replace(r"<", " ")
        except:
            pass    
        try:    
            nr = nr.replace(r">", " ")
        except:
            pass
        
        return nr

    def all_lines_Company1(self, nr, name):
        try:
            invoice_clickable = WebDriverWait(self.driver, 4).until(lambda driver: self.driver.find_elements_by_class_name("dt_open_link"))
        except:
            no_invoice.append(nr)
            quit()


        try:    
            if len(invoice_clickable) == 2:
                doubles.append(nr)
                print("o")

            elif len(invoice_clickable)>2:
                doubles.append(nr)
                # i = 0
                # y = len(invoice_clickable)
                # while i <= y:
                #     invoice_clickable = WebDriverWait(self.driver, 4).until(lambda driver: self.driver.find_elements_by_class_name("dt_open_link"))
                #     invoice_clickable[i].click()
                #     time.sleep(2)
                #     try:                        
                #         try:
                #             pdf = WebDriverWait(self.driver, 1).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[10]/span[2]/ul/li/a'))
                #         except:                     
                #             try:
                #                 pdf = WebDriverWait(self.driver, 1).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[11]/span[2]/ul/li/a'))
                #             except:
                #                 pdf = WebDriverWait(self.driver, 1).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[16]/span[2]/ul/li/a'))
                        
                #         file_name = pdf.text
                #         pdf.click()
                #         time.sleep(2)
                #         try:
                #             time.sleep(2)
                #             os.chdir(directory)
                #             os.rename(file_name,f"{name}-{i}.pdf")
                #         except:
                #             time.sleep(5)
                #             os.chdir(directory)
                #             os.rename(file_name,f"{name}-{i}.pdf")
                #         i += 1
                #         self.driver.execute_script("window.history.go(-1)")
                #         time.sleep(1)
                #     except:
                #         self.driver.execute_script("window.history.go(-1)")
                #         i+=1
                #         pass

            else:
                invoice_clickable[0].click() 
                time.sleep(2)
                x = WebDriverWait(self.driver, 1).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="pageHeader"]'))
                x = x.text
                if nr in x:
                    try:
                    
                        try:
                            pdf = WebDriverWait(self.driver, 1).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[10]/span[2]/ul/li/a'))                                                                                                                    
                        except:
                            try:
                                pdf = WebDriverWait(self.driver, 1).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[11]/span[2]/ul/li/a'))
                            except:    
                                pdf = WebDriverWait(self.driver, 1).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[16]/span[2]/ul/li/a'))

                        
                        file_name = pdf.text
                        pdf.click()
                        time.sleep(3)
                        try:
                            try:    
                                os.chdir(directory)
                                os.rename(file_name,f"{name}.pdf")
                            except:
                                time.sleep(4)
                                os.chdir(directory)
                                os.rename(file_name,f"{name}.pdf")
                        except:
                            print("error problem with naming file")

                    except:
                        try: 
                            try:
                                fil = WebDriverWait(self.driver, 1).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[15]/span[2]/a'))
                            except:
                                fil = WebDriverWait(self.driver, 1).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[16]/span[2]/a'))                                                                                          
                            
                            fil.click()
                        except:
                            print("error pobieranie")


                        try:
                            time.sleep(4)
                            os.chdir(directory)
                            files = filter(os.path.isfile, os.listdir(directory))
                            files = [os.path.join(directory, f) for f in files] # add path to each file
                            files.sort(key=lambda x: os.path.getmtime(x))
                            newest_file = files[-1]
                            os.rename(newest_file, name+".pdf")

                
                    
                        except:
                            no_attachment.append(nr)
                        
                else:
                    errors.append(nr)
                
                self.driver.execute_script("window.history.go(-1)")
        except:
            no_invoice.append(nr)
    

    def all_lines_Company2(self, nr, name):
        try:
            invoice_clickable = WebDriverWait(self.driver, 4).until(lambda driver: self.driver.find_elements_by_class_name("dt_open_link"))
        except:
            no_invoice.append(nr)
            quit()

        # fv name //*[@id="invoice_header_row_496033"]/td[1]/div/a/span
        # voided = //*[@id="invoice_header_row_496033"]/td[5]
        # approved = //*[@id="invoice_header_row_468354"]/td[5]
        try:    
            if len(invoice_clickable)>1:
                doubles.append(nr)
                # i = 0
                # y = len(invoice_clickable)
                # while i <= y:
                #     invoice_clickable = WebDriverWait(self.driver, 4).until(lambda driver: self.driver.find_elements_by_class_name("dt_open_link"))
                #     invoice_clickable[i].click()
                #     time.sleep(2)
                #     try:                        
                        
                #         try:
                #             pdf = WebDriverWait(self.driver, 2).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[14]/span[2]/ul/li/a'))
                #                                                                                                         #//*[@id="topHalf"]/div/div[1]/div[1]/section/div[14]/span[2]/ul/li/a
                #         except:
                #             try:
                #                 pdf = WebDriverWait(self.driver, 2).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[10]/span[2]/ul/li/a'))
                #             except:
                #                 pdf = WebDriverWait(self.driver, 2).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[16]/span[2]/ul/li/a'))
                        
                #         file_name = pdf.text
                #         pdf.click()
                #         time.sleep(2)
                #         try:
                #             time.sleep(2)
                #             os.chdir(directory)
                #             os.rename(file_name,f"{name}-{i}.pdf")
                #         except:
                #             time.sleep(5)
                #             os.chdir(directory)
                #             os.rename(file_name,f"{name}-{i}.pdf")
                #         i += 1
                #         self.driver.execute_script("window.history.go(-1)")
                #         time.sleep(1)
                #     except:
                #         self.driver.execute_script("window.history.go(-1)")
                #         i+=1
                #         pass

            else:
                invoice_clickable[0].click() 
                time.sleep(2)
                x = WebDriverWait(self.driver, 1).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="pageHeader"]'))
                x = x.text
                if nr in x:                  
                    try:

                        
                        try:
                            try:
                                pdf = WebDriverWait(self.driver, 2).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[14]/span[2]/ul/li/a'))
                            except:
                                pdf = WebDriverWait(self.driver, 1).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[13]/span[2]/ul/li/a'))                   
                        
                        except:
                            try:
                                pdf = WebDriverWait(self.driver, 2).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[10]/span[2]/ul/li/a'))
                            except:    
                                pdf = WebDriverWait(self.driver, 2).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[16]/span[2]/ul/li/a'))
                                                                                                                        #//*[@id="topHalf"]/div/div[1]/div[1]/section/div[16]/span[2]/ul/li/a

                        
                        file_name = pdf.text
                        pdf.click()
                        time.sleep(3)
                        try:
                            try:    
                                os.chdir(directory)
                                os.rename(file_name,f"{name}.pdf")
                            except:
                                time.sleep(4)
                                os.chdir(directory)
                                os.rename(file_name,f"{name}.pdf")
                        except:
                            print("error problem with naming file")

                    except:
                        try: 
                            try:
                                fil = WebDriverWait(self.driver, 2).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[17]/span[2]/a'))
                                                                                                                            #//*[@id="topHalf"]/div/div[1]/div[1]/section/div[17]/span[2]/a
                            except:
                                fil = WebDriverWait(self.driver, 2).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="topHalf"]/div/div[1]/div[1]/section/div[16]/span[2]/a'))                                                                                          
                            
                            fil.click()
                        except:
                            print("error pobieranie")


                        try:
                            time.sleep(4)
                            os.chdir(directory)
                            files = filter(os.path.isfile, os.listdir(directory))
                            files = [os.path.join(directory, f) for f in files] # add path to each file
                            files.sort(key=lambda x: os.path.getmtime(x))
                            newest_file = files[-1]
                            os.rename(newest_file, name+".pdf")

                
                    
                        except:
                            no_attachment.append(nr)
                else:
                    errors.append(nr)  

                self.driver.execute_script("window.history.go(-1)")
        except:
            no_invoice.append(nr)


    def final(self, FV, comp):
        try:
            self.get_site(comp)
        except:
            print("NO URL")
        try:
            self.advance_search(FV)
        except:
            print("Advance search function does not work")

        try:
            self.search()

        except:
            print("search function does not work")

        try:
            time.sleep(1)
            if comp == 1:
                self.all_lines_Company1(FV, self.name_FV(FV))
            if comp == 2:
                self.all_lines_Company2(FV, self.name_FV(FV))
        except:
            pass

        
    
    def get_missing(self):
        return no_invoice, no_attachment, doubles, errors


    def end(self):
        time.sleep(4)
        self.driver.quit()
        self.webdriver = webdriver
        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir=C:\\Users\\{user_name}\\AppData\\Local\\Google\\Chrome\\User Data")
        p = {"download.default_directory": "C:\\Users\\%s\\Downloads\\"%user_name} #, "safebrowsing.enabled":"true"
        options.add_experimental_option("prefs", p)
        self.driver = self.webdriver.Chrome(executable_path=resource_path(CHROME_DRIVER_PATH),chrome_options=options)
        self.driver.quit()
        no_invoice = []
        no_attachment = []
        doubles = []
        errors = []
            
class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.geometry("300x150")
        self.title('Coupa Automation')
        self.resizable(False,False)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=3)
        self.columnconfigure(3, weight=3)
        self.columnconfigure(4, weight=3)
        self.columnconfigure(5, weight=3)
        self.columnconfigure(6, weight=3)
        self.create_widgets()



    def create_widgets(self):
        # FV list
        company_list_label = ttk.Label(self, text="Paste document list")
        company_list_label.grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)
        
        global company_list_entry
        company_list_entry = ttk.Entry(self)
        company_list_entry.grid(column=1, row=0, sticky=tk.NSEW, padx=10, pady=10)

        search_button = ttk.Button(self, text="Begin Search", command=self.Start_and_get_data)
        search_button.grid(column=1, row=3, sticky=tk.NSEW, padx=5, pady=5)

        global mode_on_button  
        mode_on_button = ttk.Combobox(self,values=['Company1', 'Company2'])
        mode_on_button.grid(column=1, row=4, sticky=tk.NSEW, padx=10, pady=10)
        mode_on_button.current(1)

        global dir_button
        dir_button = ttk.Button(self, text="Save to", command = self.get_dir)
        dir_button.grid(column=0, row = 4, sticky=tk.NSEW, padx=5,pady=5)



    def Start_and_get_data(self):
        mode = mode_on_button.get()
        self.update_idletasks()
        lista = company_list_entry.get()
        if "\n" in lista:
            lista = list(lista.split("\n"))            
            lista = list(dict.fromkeys(lista))
            lista = lista[:-1]
        else:
            tk.messagebox.showerror("Fatal Error", "Please provide correct data format")

        try:    
            test = directory
            print(test)
        except:
            tk.messagebox.showerror("Fatal Error", "Backend error")

        work = Program(test)     

        try:
            i = 0
            y = len(lista)-1
            while i <= y:
                latest_FV = lista[i]
                print(latest_FV)
                if mode == "Company1":
                    work.final(latest_FV, 1)
                if mode == "Company2":
                    work.final(latest_FV, 2)
                i+=1                
            missing_documents, missing_attachments, doubles, errors = work.get_missing()
            self.pop_wind(missing_documents, missing_attachments, doubles, errors)
            work.end()
        except:
            tk.messagebox.showerror("Fatal Error", "Backend error")





    def pop_wind(self, one, two, td, fr):

        response = messagebox.askyesno(title='Proces finished', message="""Do you want to generate Exel report?\nNo document in tax year:{one} 
No attachment: {two}\nDoubles:{tree}\nErrors:{fr}""".format(one=one, two=two, tree=td, fr=fr))
        if response == True:
            raport = pd.DataFrame([one,two,td, fr], index=['No invoice','Missing attachment','Doubles', 'Errors'])
            raport = raport.transpose()
            raport.to_excel('raport_from_Coupa.xlsx', sheet_name='Missing data')

        self.create_widgets()


    def get_dir(self):
        global directory
        directory = filedialog.askdirectory()
        # print(directory)
        return directory



if __name__ == "__main__":
    app = App()
    app.mainloop()

