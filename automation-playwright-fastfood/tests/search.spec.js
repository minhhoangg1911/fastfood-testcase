const { test } = require('@playwright/test');

test('Search Orders Test', async ({ page }) => {
    await page.goto('http://localhost:3000/admin');

    await page.locator("//span[contains(text(), 'All Orders')]").click();

    await page.locator('[name="searchString"]').fill('customer');

    await page.locator("//button[contains(text(), 'Filters')]").click();
});
