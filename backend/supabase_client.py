#import os
#from supabase import create_client, Client

#SUPABASE_URL = os.getenv("https://zkxbqzvtrfybwgeydixp.supabase.co")
#SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpreGJxenZ0cmZ5YndnZXlkaXhwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1Nzc4NjM1NiwiZXhwIjoyMDczMzYyMzU2fQ._5Ee6NYke1o5Wp1fx7PhIHu-obeDuDPx2ac6CA94xic")

#supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


from supabase import create_client, Client
import os

# -------------------------
# Supabase Configuration
# -------------------------
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://zkxbqzvtrfybwgeydixp.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpreGJxenZ0cmZ5YndnZXlkaXhwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1Nzc4NjM1NiwiZXhwIjoyMDczMzYyMzU2fQ._5Ee6NYke1o5Wp1fx7PhIHu-obeDuDPx2ac6CA94xic")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

print("✅ Supabase client initialized successfully!")
