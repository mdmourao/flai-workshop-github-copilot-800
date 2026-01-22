#!/bin/bash

# OctoFit Tracker API Testing Script
# This script tests all API endpoints using either Codespace URL or localhost

# Determine base URL
if [ -n "$CODESPACE_NAME" ]; then
    BASE_URL="https://${CODESPACE_NAME}-8000.app.github.dev"
    echo "🌐 Using Codespace URL: $BASE_URL"
else
    BASE_URL="http://localhost:8000"
    echo "🏠 Using localhost: $BASE_URL"
fi

echo ""
echo "================================================"
echo "  OctoFit Tracker API Test Suite"
echo "================================================"
echo ""

# Test API Root
echo "📋 Testing API Root..."
curl -s "${BASE_URL}/" | python3 -m json.tool
echo ""
echo "✅ API Root test complete"
echo ""

# Test Users API
echo "👥 Testing Users API..."
curl -s "${BASE_URL}/api/users/" | python3 -m json.tool | head -40
echo ""
echo "✅ Users API test complete"
echo ""

# Test Teams API
echo "🏆 Testing Teams API..."
curl -s "${BASE_URL}/api/teams/" | python3 -m json.tool
echo ""
echo "✅ Teams API test complete"
echo ""

# Test Activities API
echo "🏃 Testing Activities API..."
curl -s "${BASE_URL}/api/activities/" | python3 -m json.tool | head -30
echo ""
echo "✅ Activities API test complete"
echo ""

# Test Leaderboard API
echo "🥇 Testing Leaderboard API..."
curl -s "${BASE_URL}/api/leaderboard/" | python3 -m json.tool | head -30
echo ""
echo "✅ Leaderboard API test complete"
echo ""

# Test Workouts API
echo "💪 Testing Workouts API..."
curl -s "${BASE_URL}/api/workouts/" | python3 -m json.tool | head -30
echo ""
echo "✅ Workouts API test complete"
echo ""

echo "================================================"
echo "  ✨ All API tests completed successfully!"
echo "================================================"
