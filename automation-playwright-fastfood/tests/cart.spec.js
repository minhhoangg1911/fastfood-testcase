const { test, expect } = require('@playwright/test');

test('Cart Flow Test', async ({ page }) => {


    await page.goto('http://localhost:3000');
    // ---- CART ----
    const addCartButton = page.locator("//i[contains(@class, 'bi-cart-plus')]").first();
    await addCartButton.scrollIntoViewIfNeeded();
    await addCartButton.click();

    const toast = page.locator("//div[contains(text(),'Item added to cart successfully')]");
    await expect(toast).toBeVisible();
    await toast.click();

    const cartLink = page.locator("//a[contains(text(), 'Cart')]");
    await cartLink.scrollIntoViewIfNeeded();
    await cartLink.click();

    await page.locator("//i[contains(@class, 'bi bi-plus-circle-fill')]").click();
    await page.locator("//i[contains(@class, 'bi bi-dash-circle-fill')]").click();
    await page.locator('[name="phoneNumber"]').fill('0987654321');

    const placeOrderBtn = page.locator("//button[@type='submit']");
    await placeOrderBtn.click();

    // ---- PAYMENT ----
    await page.goto('http://localhost:3000/payment');

    const frame = page.frameLocator("iframe[title='Secure payment input frame']");
    await frame.locator("#Field-numberInput").fill("4111111111111111");
    await frame.locator("#Field-expiryInput").fill("02/26");
    await frame.locator("#Field-cvcInput").fill("123");
    await frame.locator("#Field-countryInput").selectOption({ label: "United States" });
    await frame.locator("#Field-postalCodeInput").fill("44444");

    const submitBtn = page.locator("//button[.//span[text()='Submit Order']]");
    await submitBtn.scrollIntoViewIfNeeded();
    await submitBtn.click();


});