#Script for calculationg remaining credits

from client import RestClient
import json

client = RestClient("yasir@programmx.com", "2cd75ad6a1045655")

# Check account balance and limits
response = client.get("/v3/appendix/user_data")

if response.get("status_code") == 20000:
    result = response.get("tasks", [{}])[0].get("result", [{}])[0]
    money = result.get("money", {})
    
    # Calculate spent from total - balance
    total_deposited = money.get("total", 0)
    balance = money.get("balance", 0)
    total_spent = total_deposited - balance
    
    print("=" * 50)
    print("       DATAFORSEO ACCOUNT INFO")
    print("=" * 50)
    print(f"Login:              {result.get('login', 'N/A')}")
    print(f"Timezone:           {result.get('timezone', 'N/A')}")
    print("-" * 50)
    print(f"Total Deposited:    ${total_deposited:.2f}")
    print(f"Current Balance:    ${balance:.2f}")
    print(f"Total Spent:        ${total_spent:.2f}")
    print("-" * 50)
    
    # Backlinks subscription info
    backlinks_expiry = result.get("backlinks_subscription_expiry_date", "N/A")
    print(f"Backlinks Expires:  {backlinks_expiry}")
    print("=" * 50)
    
else:
    print("Error:", response.get("status_message", "Unknown error"))