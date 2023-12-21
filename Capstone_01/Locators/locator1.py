class Orange_locat:

   #OrangeHRM Login Xpath
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    user_name = "username"
    pass_name = "password"
    login_xpath = '//div[@class="oxd-form-actions orangehrm-login-action"]//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]'
    dash_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    user_drop_xpath ='/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p'
    invalid_credits_xp = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'
    logout_xpath = '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'
    
# Employee Personal Details 

    pim_xpath = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    add_button_xp ='/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    first_name = "firstName"
    last_name = "lastName"
    employee_login_xp ='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
    employee_user_xp = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    employee_password_xp = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    confirm_password_xp = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    save_button_xp = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'

    other_id_xp = '//form/div[2]/div[1]/div[2]/div/div[2]/input'
    driving_licencse_xp = '//form/div[2]/div[2]/div[1]/div/div[2]/input' 
    license_expiry_xp = '//form/div[2]/div[2]/div[2]/div/div[2]/div/div/input[@class="oxd-input oxd-input--active"]'
    ssn_xp = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    sin_xp = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    nationality_drop = '//label[text()="Nationality"]/parent::div/following-sibling::div//i'
    nationality_xp =  '//div[@class="oxd-select-wrapper"]//div[@class="oxd-select-dropdown --positon-bottom"]//span[text()="Afghan"]'
    dateofbirth_xp = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
    gender_rad_xp = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span'
    militaryservice_xp = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
    personal_detail_save_xp = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'

# Employee Personal Details Edit

    employee_list_xp = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a'
    employee_search_name_xp = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    header_xp = '//div[@class="oxd-topbar-header-title"]'
    employee_search_button = '//form/div[2]/button[2]'
    record_display = '//div[contains(text(),"Pageedrid")]'

    edit_button_xp = '//div[@role="table"]//div[1]//div[1]//div[9]//div[1]//button[2]//i[1]'
    ssn_edit_xp = '//form/div[2]/div[3]/div[1]/div/div[2]/input'
    martial_status_dd_xp = '//label[text()="Marital Status"]/parent::div/following-sibling::div//i'
    martial_status_dop_xp = '//div[@class="oxd-select-wrapper"]//div[@class="oxd-select-dropdown --positon-bottom"]'
    martial_status_dop_single_xp = '//div[@class="oxd-select-wrapper"]//div[@class="oxd-select-dropdown --positon-bottom"]//span[text()="Married"]'
    blood_type_dd_xp = '//label[text()="Blood Type"]/parent::div/following-sibling::div//i'
    blood_type_ap_xp = '//div[@class="oxd-select-wrapper"]//div[@class="oxd-select-dropdown --positon-bottom"]//span[text()="A+"]'
    custom_save_xp = '(//div[@class="oxd-layout-context"]//form)[2]//button'

   
# Deleting the Employee Details
    
    delete_icon_xp = '//div[@role="table"]//div[1]//div[1]//div[9]//div[1]//button[1]//i'
    delete_button_xp = '//div/div/div[3]/button[2]'
    no_record_xp = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span'