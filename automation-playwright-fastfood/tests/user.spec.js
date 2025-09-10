const { test, expect } = require('@playwright/test');

test('Delete User Test', async ({ page }) => {
    await page.goto('http://localhost:3000/admin'); // đổi URL thật

    const userLink = page.locator("//span[contains(text(), 'List User')]");
    await userLink.scrollIntoViewIfNeeded();
    await userLink.click();

    const deleteButton = page.locator(
        "//div[@class='row border' and .//div[text()='customer1@gmail.com']]//button[contains(@class,'btn-danger')]"
    );
    await deleteButton.scrollIntoViewIfNeeded();
    await deleteButton.click();

});
