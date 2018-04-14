from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
from config import user
from db import Job
import time
import os

driver = None


def init(job):
    time.sleep(1)
    driver.get(job.url)
    if driver.find_elements_by_class_name("indeed-apply-button"):
        elem = driver.find_elements_by_class_name("indeed-apply-button")[0]
        elem.click()
        time.sleep(1)
        iframe = driver.find_element_by_xpath(
            "//*[@class='indeed-apply-bd']/iframe")
        driver.switch_to_frame(iframe)
        time.sleep(1)
        iframe = driver.find_element_by_xpath("/html/body/iframe")
        driver.switch_to_frame(iframe)
        complete_step_one(job)
        # driver.close()
    else:
        Job.update(applied=True).where(Job.applied == True).execute()


def complete_step_one(job):
    name = user.get('first_name') + ' ' + user.get('last_name')
    cover_letter_body = """
Dear Hiring Manager,

Hello, my name is {name}. Nice to meet you!

I have 5+ years of experience as a Front-End/Full-stack Engineer with skills Angular, React, PHP, NodeJS, python and etc. I'd really love the opportunity to interview at  {company_name} for the open {job_title} position.

Thanks again. You can reach me at {phone_number} if you'd like to chat.

Sincerely,
{name}
  """.format(
        name=name,
        linkedin=user.get('linkedin'),
        company_name=job.company,
        job_title=job.title,
        phone_number=user.get('phone'),
        github=user.get('github')
    )

    time.sleep(5)
    try:
        elem = driver.find_element_by_name("applicant.firstName")
        elem.send_keys(user.get('first_name'))
        elem = driver.find_element_by_name("applicant.lastName")
        elem.send_keys(user.get('last_name'))
    except common.exceptions.NoSuchElementException:
        elem = driver.find_element_by_name('applicant.name')
        elem.send_keys(name)

    elem = driver.find_element_by_xpath('//*[@id="input-applicant.email"]')
    elem.send_keys(user.get('email'))

    elem = driver.find_element_by_xpath(
        '//*[@id="input-applicant.phoneNumber"]')
    elem.send_keys(user.get('phone'))

    elem = driver.find_element_by_xpath('//*[@id="ia-FilePicker-resume"]')
    elem.send_keys(os.getcwd()+"/resume_dimpu_buddha_Front_END.pdf")

    try:
        elem = driver.find_element_by_xpath(
        '//*[@id="textarea-applicant.applicationMessage"]')
        elem.send_keys(cover_letter_body)
    except:
        print("NO Cover letter")
    # time.sleep(10)
    try:
        driver.find_element_by_xpath('//*[@id="form-action-submit"]').click()
    except:
        driver.find_element_by_xpath('//*[@id="form-action-continue"]').click()
    continue_steps(job)
    update_applied(job)

def continue_steps(job):



def answer_text_questions(job)
    # should only be running on required questions
    answers = {
      'projects' : "I actually built a json based from builder using Angular,Redux : next-forms.techumber.com",
      'Website' : "http://www.techumber.com/",
      'experience': 5,
      'LinkedIn' : confit.user.linkedin,
      'How did you hear about this job?' : 'indeed.com',
      'salary expectations' : '$80,000',
      'How did you hear about this job?' : 'indeed.com',
      'Github' : config.user.github,
      'In 150 characters or fewer, tell us what makes you unique. Try to be creative and say something that will catch our eye!' : "I am a driven individual that will not stop until I find a solution to any type of problem.",
      'What are your salary requirements (excluding bonus, commission, equity)?' : 'Entry-Level',
      'Address Line' : '214 William St, Apt. 2',
      'City' : 'Harrison',
      'State' : 'New Jersery'
    }
    fields = driver.find_element_by_xpath("//textarea|//input")
    for field in fields:
        question = field.find(:xpath, "..").find(:xpath, "..").find('label')
        # see if any of the question is 'answerable' with answers.
        answers.keys.each do |question_we_can_answer|
          if question.text.include? question_we_can_answer
            fill_in field['name'], with: answers[question_we_can_answer]


# only complete required fields (skip optional)
# def complete_additional_steps():
#   for label in driver.find_elements_by_xpath('//label'):
    # if 'optional' not in label.text:
#       # answer_radio_questions()
#       # answer_text_questions
#       if driver.find_elements_by_css_selector('a.button_content.form-page-next'):
#         driver.find_elements_by_css_selector('a.button_content.form-page-next').click()
#         time.sleep(1)
#       else:

    #   # only complete required fields (skip optional)
    #   all('label').each do |field|
    #     if !field.text.include? 'optional'
    #       answer_radio_questions
    #       answer_text_questions
    #       if page.has_selector?('a.button_content.form-page-next')
    #         page.find('a.button_content.form-page-next', match: :first).click
    #         sleep(1)
    #       end
    #     elsif page.has_selector?('a.button_content.form-page-next')
    #       page.find('a.button_content.form-page-next', match: :first).click
    #       sleep(1)
    #       complete_additional_steps
    #     end
    #   end
    #   until page.has_selector?('input#apply')
    #     complete_additional_steps
    #   end
    #   apply
    # end

def update_applied(job):
    job.applied = True
    job.save()


# def main():
#     for job in Job.select().where(Job.applied == False):
#         print(job.title)
#         print(job.applied)
#         print(job.url)
#         global driver
#         if driver is None:
#             driver = webdriver.Firefox()
#             init(job)
#         else:
#             update_applied(job)


driver = webdriver.Firefox()

def main():
    for job in Job.select().where(Job.applied == False):
        print(job.title)
        print(job.applied)
        print(job.url)
        try:
            init(job)
        except:
            init(job)


main()


#driver.close()
