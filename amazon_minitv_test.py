import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()                         # Maximizing the browser
    driver.get("https://www.amazon.in/minitv")       # Launching the url
    driver.implicitly_wait(10)                       # Implicit wait for 10 seconds
    yield driver


def test_open_amazon_minitv(driver):
    # Task 1: Opening Amazon MiniTV
    driver.get("https://www.amazon.in/minitv")
    assert 'Watch Free Web Series & Short Films Online | Amazon miniTV' in driver.title


def test_select_series(driver):
    # Task 2: Finding and Selecting a Series
    series_link = driver.find_element(By.XPATH, "//img[@alt='Yeh Meri Family - Season 2 - Watch Free']")
    series_link.click()
    time.sleep(5)
    assert "https://www.amazon.in/minitv" in driver.current_url


def test_play_season_one_first_episode(driver):
    # Task 3: Playing the First Episode of Season 1
    series_link = driver.find_element(By.XPATH, "//img[@alt='Yeh Meri Family - Season 2 - Watch Free']")
    series_link.click()

    seasons = driver.find_element(By.XPATH, "//div[@id='m-tabs-0-1']//h2[contains(@class,'Heading_h2__DveuA "
                                            "SeasonsTab_tabHeading__mGwNN')][contains(text(),'Season')]")
    seasons.click()
    time.sleep(5)

    first_episode = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div["
                                                  "1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]/div[1]/span["
                                                  "1]/span[1]/img[1]")
    first_episode.click()
    time.sleep(10)  # Adding a delay of 10 seconds to check the video is playing

    # Verify video playback
    video_element = driver.find_element(By.XPATH, "//video")
    assert video_element.is_displayed()


def test_play_season_two_first_episode(driver):
    #  Playing the First Episode of Season 2
    series_link = driver.find_element(By.XPATH, "//img[@alt='Yeh Meri Family - Season 2 - Watch Free']")
    series_link.click()

    seasons_two = driver.find_element(By.XPATH, "//div[@id='m-tabs-0-0']//h2[contains(@class,'Heading_h2__DveuA "
                                                "SeasonsTab_tabHeading__mGwNN')][contains(text(),'Season')]")
    seasons_two.click()
    time.sleep(5)

    first_episode = driver.find_element(By.XPATH, "//span[@class='ThumbnailCard_iconContainer___2qS6']//span["
                                                  "@class='ThumbnailCard_playIconContainer__IkFPt']//img")
    first_episode.click()

    time.sleep(10)    # Adding a delay of 10 seconds to check the video is playing

    # Verify video playback
    video_element = driver.find_element(By.XPATH, "//video")
    assert video_element.is_displayed()


if __name__ == '__main__':
    pytest.main(["-v", "amazon_minitv_test.py"])
