from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector as mysql
import os
import json