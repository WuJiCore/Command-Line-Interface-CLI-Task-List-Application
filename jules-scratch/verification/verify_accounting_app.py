from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Login as admin
    page.goto("http://127.0.0.1:8000/login/")
    page.wait_for_load_state()
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'password')
    page.click('button[type="submit"]')
    page.wait_for_load_state()

    # Create employee
    page.goto("http://127.0.0.1:8000/create_employee/")
    page.wait_for_load_state()
    page.wait_for_selector('select[name="role"]')
    page.fill('input[name="username"]', 'employee')
    page.fill('input[name="password"]', 'password')
    page.select_option('select[name="role"]', 'employee')
    page.click('button[type="submit"]')
    page.wait_for_load_state()

    # Login as employee
    page.goto("http://127.0.0.1:8000/login/")
    page.wait_for_load_state()
    page.fill('input[name="username"]', 'employee')
    page.fill('input[name="password"]', 'password')
    page.click('button[type="submit"]')
    page.wait_for_load_state()

    # Add sale
    page.goto("http://127.0.0.1:8000/add_sale/")
    page.wait_for_load_state()
    page.fill('input[name="date"]', '2025-10-30')
    page.fill('input[name="product"]', 'Test Product')
    page.fill('input[name="quantity"]', '1')
    page.fill('input[name="price"]', '10.00')
    page.fill('input[name="total"]', '10.00')
    page.click('button[type="submit"]')
    page.wait_for_load_state()

    # Request edit
    page.goto("http://127.0.0.1:8000/view_data/")
    page.wait_for_load_state()
    page.click('a:has-text("Request Edit")')
    page.wait_for_load_state()
    page.fill('textarea[name="reason"]', 'Test Reason')
    page.fill('textarea[name="requested_changes"]', 'quantity=2, total=20.00')
    page.click('button[type="submit"]')
    page.wait_for_load_state()

    # Login as admin
    page.goto("http://127.0.0.1:8000/login/")
    page.wait_for_load_state()
    page.fill('input[name="username"]', 'admin')
    page.fill('input[name="password"]', 'password')
    page.click('button[type="submit"]')
    page.wait_for_load_state()

    # View admin dashboard
    page.goto("http://127.0.0.1:8000/admin_dashboard/")
    page.wait_for_load_state()
    page.screenshot(path="jules-scratch/verification/verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
