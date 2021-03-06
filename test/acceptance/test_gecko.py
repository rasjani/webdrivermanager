import sys
from flaky import flaky

from .tools import SRC_ROOT, AutomaticBaseTest, ExplicitBaseTest, NO_FILE, NO_LINK_FILE

sys.path.append(SRC_ROOT)
import webdrivermanager  # noqa: E402 I001


class GeckoDriverManagerTestsWithAutomaticLocations(AutomaticBaseTest):
    DRIVER_MANAGER = webdrivermanager.GeckoDriverManager

    @flaky
    def test_download(self):
        self.instance = self.DRIVER_MANAGER()
        filename = self.instance.download(show_progress_bar=False)
        self.assertTrue(filename.is_file(), NO_FILE)

    @flaky
    def test_download_and_install(self):
        self.instance = self.DRIVER_MANAGER()
        driver_link_target, driver_binary = self.instance.download_and_install(show_progress_bar=False)
        self.assertTrue(driver_binary.is_file(), NO_FILE)
        self.assertTrue(driver_link_target.is_file(), NO_LINK_FILE)


class GeckoDriverManagerTestsWithExplicitLocations(ExplicitBaseTest):
    DRIVER_MANAGER = webdrivermanager.GeckoDriverManager

    @flaky
    def test_download(self):
        self.instance = self.DRIVER_MANAGER(download_root=self.temp_dir.name)
        filename = self.instance.download(show_progress_bar=False)
        self.assertTrue(filename.is_file(), NO_FILE)

    @flaky
    def test_download_and_install(self):
        link_path = self.make_link_dir()
        self.instance = self.DRIVER_MANAGER(download_root=self.temp_dir.name, link_path=link_path)
        driver_link_target, driver_binary = self.instance.download_and_install(show_progress_bar=False)
        self.assertTrue(driver_binary.is_file(), NO_FILE)
        self.assertTrue(driver_link_target.is_file(), NO_LINK_FILE)
