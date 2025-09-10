const { test, expect } = require('@playwright/test');

test('Food Page Test', async ({ page }) => {
    await page.goto('http://localhost:3000/admin'); // đổi URL thực tế

    await page.locator("//span[@class='ant-menu-title-content' and text()='Food']").click();

    await page.locator("[name='name']").fill("Burgur");

    await page.locator("//textarea[@name='description']").fill("Món Ăn Ngon");

    await page.locator("[name='specialTag']").fill("XXX");

    await page.locator("[name='category']").selectOption("Dessert");

    await page.locator("[name='price']").fill("20");

    const filePath = "C:/Users/Admin/Downloads/airplane_0005.jpg";
    await page.locator("#file").setInputFiles(filePath);

    const createButton = page.locator("//button[contains(text(), 'Create')]");
    await createButton.scrollIntoViewIfNeeded();
    await createButton.click();

    const listFood = page.locator("//span[@class='ant-menu-title-content' and text()='List Food']");
    await listFood.scrollIntoViewIfNeeded();
    await listFood.click();

    const deleteButtons = page.locator("button.btn-danger");
    const count = await deleteButtons.count();
    if (count > 0) {
        const lastButton = deleteButtons.nth(count - 1);
        await lastButton.scrollIntoViewIfNeeded();
        await lastButton.click();
    }

});
