const { test, expect } = require('@playwright/test');

test('Login Test', async ({ page }) => {
    await page.goto('http://localhost:3000');
    // await page.locator("//div[contains(text(),'Register successful! Please login to continue')]").click();
    await page.locator("//a[text()='Setting']").click();
    await page.locator("//a[text()='Login']").click();

    await page.locator("[name='userName']").fill('admin1@gmail.com');
    await page.locator("//input[@type='password']").fill('123456');
    await page.locator("//button[contains(text(),'Login')]").click();

    // Lưu session ra file JSON
    await page.context().storageState({ path: 'storageState.json' });
});