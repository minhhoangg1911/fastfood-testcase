const { test, expect } = require('@playwright/test');


test.use({ storageState: undefined }); // không load state cũ


test('Register Test', async ({ page }) => {
    await page.goto('http://localhost:3000');

    await page.locator("//a[text()='Setting']").click();

    await page.locator("//a[text()='Register']").click();

    await page.locator("[name='userName']").fill("customer1@gmail.com");

    await page.locator("[name='name']").fill("customer1");

    await page.locator("//input[@type='password']").fill("123456");

    await page.locator("[name='role']").selectOption({ label: "Customer" });

    await page.locator("//button[contains(text(),'Register')]").click();

});
