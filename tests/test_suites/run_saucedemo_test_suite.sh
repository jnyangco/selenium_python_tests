#!/usr/bin/env bash
echo "🚀 Running Saucedemo Tests..."

pytest -s -v -m ui --browser=chrome --env=docker -n auto
#pytest -s -v -m ui --browser=chrome --env=docker --alluredir=reports/allure-results -n auto