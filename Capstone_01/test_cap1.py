from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import datetime
import pytest
import time
from Data import data1
from Locators import locator1

class Test_Capstoneorg:

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(20)
        self.wait = WebDriverWait(self.driver, 40)
        self.driver.get(locator1.Orange_locat().url)
        self.driver.maximize_window()
        yield
        self.driver.close()

    # Common Login Function Used for Test Cases

    def perform_login(self, username, password):
        username_info = self.wait.until(
            EC.element_to_be_clickable((By.NAME, locator1.Orange_locat().user_name)))
        username_info.send_keys(username)

        password_info = self.wait.until(
            EC.element_to_be_clickable((By.NAME, locator1.Orange_locat().pass_name)))
        password_info.send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, locator1.Orange_locat().login_xpath))).click()

     # Check for the valid and Invalid Credentials of OrangeHRM
    
    def test_login(self, booting_function):
        try:
            for row in range(2, 4):
                username = org.access_data(row, 5)
                password = org.access_data(row, 6)

                self.perform_login(username, password)
                
                dash = locator1.Orange_locat().dash_url
                dashboard_url = self.driver.current_url
                current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


                if dash in dashboard_url:
                    org.write_data(row, 8, current_datetime)
                    org.write_data(row, 9, "Login Passed")
                    assert dash == dashboard_url, f"Dashboard URL mismatch for login data: {username}, {password}"

                    self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, locator1.Orange_locat().user_drop_xpath))).click()

                    self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, locator1.Orange_locat().logout_xpath))).click()
                    self.driver.refresh()
                    print("Login Passed with data: ", username, password)

                else:
                    invalid_message = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, locator1.Orange_locat().invalid_credits_xp)))
                    assert invalid_message.is_displayed(), f"Error Message is not Displayed"
                    org.write_data(row, 8, current_datetime)
                    org.write_data(row, 9, "Login Failed")
                    screenshot_directory3 = r"E:\Automation Testing\practice\Task\Capstone_01\Screenshots"
                    screenshot_filename3 = "Invalid_data.png"
                    screenshot_path3 = f"{screenshot_directory3}\\{screenshot_filename3}"
                    self.driver.save_screenshot(screenshot_path3)
                    print("Error Message is displayed as: ", invalid_message.text)


        except Exception as e:
            print("Login error on: ", e)

    # Test Case for Adding Editing & Deleting Employee's Personal Details

    def test_addemployee(self, booting_function):
        try:
            username1 = org.access_data(2, 5)
            password1 = org.access_data(2, 6)

            self.perform_login(username1,password1)
            current_datetime1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Creating Variables for the web elements of OrangeHRM for adding Personal Details for the Employee

            pim1 = locator1.Orange_locat().pim_xpath 
            add1 =  locator1.Orange_locat().add_button_xp 
            employee_name1 = locator1.Orange_locat().first_name  
            employee_name2 = locator1.Orange_locat().last_name  
            employee_log = locator1.Orange_locat().employee_login_xp 
            employee_username =locator1.Orange_locat().employee_user_xp 
            employee_password = locator1.Orange_locat().employee_password_xp
            confirm_pass = locator1.Orange_locat().confirm_password_xp 
            employee_save = locator1.Orange_locat().save_button_xp 
            Driving_licencse = locator1.Orange_locat().driving_licencse_xp 
            Driving_expiry = locator1.Orange_locat().license_expiry_xp 
            other_id = locator1.Orange_locat().other_id_xp
            ssn_no = locator1.Orange_locat().ssn_xp
            sin_no = locator1.Orange_locat().sin_xp 
            nationality_drop1 = locator1.Orange_locat().nationality_drop 
            nationality1 = locator1.Orange_locat().nationality_xp 
            Date_of_Birth =locator1.Orange_locat().dateofbirth_xp  
            gender = locator1.Orange_locat().gender_rad_xp 
            military = locator1.Orange_locat().militaryservice_xp
            personal_save = locator1.Orange_locat().personal_detail_save_xp 

# Accesing Excel File & Store the data of Employee to the Variable for working

            emp_name1_data = org.access_data(11, 2)
            emp_name2_data = org.access_data(11, 5)
            emp_login_name = org.access_data(11, 3)
            emp_login_password = org.access_data(11, 4)
            licensce_no = org.access_data(15, 1)
            license_expiry = org.access_data(15, 2)
            other_id_data = org.access_data(15, 8)
            ssn_data = org.access_data(15, 3)
            sin_data = org.access_data(15, 4)
            birthdate = org.access_data(15, 5)
            military_data =org.access_data(15, 6)

# Making Dictonary using Emloyee Personal Details web Elements And Data as Key & Value Pair 

            emplyoee_personal = {
                pim1:None,
                add1:None,
                employee_name1:emp_name1_data,
                employee_name2:emp_name2_data,
                employee_log:None,
                employee_username:emp_login_name,
                employee_password:emp_login_password,
                confirm_pass:emp_login_password,
                employee_save:None,
                other_id:other_id_data,
                ssn_no:ssn_data,
                sin_no:sin_data,
                nationality_drop1:None,
                nationality1:None,
                gender:None,
                military:military_data    
            }

# By iterating the Dictonary we can fill the inputs for Personal Details for employee

            for element_locators, values in emplyoee_personal.items():
                try:
                    if values is not None:
                        if '/' in element_locators:
                            element = self.wait.until(
                                EC.element_to_be_clickable((By.XPATH, element_locators)))
                        else:
                            element = self.wait.until(
                                EC.element_to_be_clickable((By.NAME, element_locators)))
                        
                        
                        element.send_keys(values)
                        print(f"Set value '{values}' for element with locator: {element_locators}")   
                    
                    else:
                        if '/' in element_locators:
                            button = self.wait.until(
                                EC.element_to_be_clickable((By.XPATH, element_locators)))
                        else:
                            button = self.wait.until(
                                EC.element_to_be_clickable((By.NAME, element_locators)))

                        button.click()
                        print(f"Clicked the button with locator: {element_locators}")

                except Exception as e:
# Handle exceptions if the element is not found or other issues
                    print(f"Error interacting with element with locator {element_locators}: {str(e)}")
                    print(f"Locator {element_locators} did not work as expected.")

            
            driving_data1 = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, Driving_licencse)))
            driving_data1.click()
            driving_data1.send_keys(licensce_no)

            self.driver.execute_script(f"arguments[0].value = '{license_expiry}';", self.wait.until(
                EC.element_to_be_clickable((By.XPATH, Driving_expiry))))
           
            self.driver.execute_script(f"arguments[0].value = '{birthdate}';", self.wait.until(
                EC.element_to_be_clickable((By.XPATH, Date_of_Birth))
            ))
            
            details_save = self.wait.until(EC.element_to_be_clickable((By.XPATH, personal_save)))
            details_save.click()

# Click on the employee list tab to search for the employee

            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator1.Orange_locat().employee_list_xp))).click()

            search_name = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator1.Orange_locat().employee_search_name_xp)))
            search_name.click()
            search_name.send_keys(emp_name1_data)

            serach_button1 =  self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator1.Orange_locat().employee_search_button)))
            serach_button1.click()

            search_record1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locator1.Orange_locat().record_display)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", search_record1)

            assert search_record1.text in emp_name1_data, f"Expected '{search_record1.text}' to be in '{emp_name1_data}', but it's not."
            print("Search Record Found on: ", search_record1.text)

 #screenshot for employee added

            screenshot_directory = r"E:\Automation Testing\practice\Task\Capstone_01\Screenshots"
            screenshot_filename = "employee_added.png"
            screenshot_path = f"{screenshot_directory}\\{screenshot_filename}"
            self.driver.save_screenshot(screenshot_path)

            org.write_data(4, 8, current_datetime1)
            org.write_data(4, 9, "Emplyoee data Added")

# Click on the Edit icon to make Edits in the personal Detais

            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator1.Orange_locat().edit_button_xp))).click()

            ssn_edit = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator1.Orange_locat().ssn_edit_xp)))
            ssn_edit.send_keys(Keys.BACKSPACE * len(ssn_edit.get_attribute("value")))
            ssn_edit_data = org.access_data(15, 7)
            ssn_edit.send_keys(ssn_edit_data)

            marital_status = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locator1.Orange_locat().martial_status_dd_xp)))
            marital_status.click()

            self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, locator1.Orange_locat().martial_status_dop_xp)))
            marital_status_single = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator1.Orange_locat().martial_status_dop_single_xp)))
            marital_status_single.click()


            blood_type_drop = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator1.Orange_locat().blood_type_dd_xp)))
            blood_type_drop.click()

            blood_type_data = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator1.Orange_locat().blood_type_ap_xp)))
            blood_type_data.click()

            custom_save = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator1.Orange_locat().custom_save_xp)))
            custom_save.click()


            edited_value = ssn_edit.get_attribute("value")
            assert edited_value == str(ssn_edit_data), f"Expected '{ssn_edit_data}' to be in '{ssn_edit.text}', but it is not"
            print("Data Edited Successfully")

# wrtie data to excel

            org.write_data(5, 8, current_datetime1)
            org.write_data(5, 9, "Emplyoee data Edited")

            details_save = self.wait.until(EC.element_to_be_clickable((By.XPATH, personal_save)))
            details_save.click()

#  deleting the record

            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator1.Orange_locat().employee_list_xp))).click()

            search_name = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator1.Orange_locat().employee_search_name_xp)))
            search_name.click()
            search_name.send_keys(emp_name1_data)

            serach_button1 =  self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator1.Orange_locat().employee_search_button)))
            serach_button1.click()

            search_record1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locator1.Orange_locat().record_display)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", search_record1)

# Click on the Delete Icon to Delete the record
    
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locator1.Orange_locat().delete_icon_xp))).click()

            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locator1.Orange_locat().delete_button_xp))).click()


            no_record = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locator1.Orange_locat().no_record_xp)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", no_record)

            assert no_record.is_displayed()
            expected_no_record = org.access_data(18, 7)
            assert no_record.text == expected_no_record, f"Expected '{expected_no_record}'not in '{no_record.text}'"
            print("Deleted Successfully: ", no_record.text)

            screenshot_directory2 = r"E:\Automation Testing\practice\Task\Capstone_01\Screenshots"
            screenshot_filename2 = "employee_deleted.png"
            screenshot_path2 = f"{screenshot_directory2}\\{screenshot_filename2}"
            self.driver.save_screenshot(screenshot_path2)

            org.write_data(6, 8, current_datetime1)
            org.write_data(6, 9, "Emplyoee data Deleted")
            
                    
        except Exception as e:
            print("Employee Deletion error on: ", e)

    

excel_file = r"E:\Automation Testing\practice\Task\Capstone_01\capdate.xlsx"
sheet_name = "Sheet1"
org = data1.Orange_dat(excel_file, sheet_name)
max_row = org.row_count()































































