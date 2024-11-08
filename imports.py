from flask import Flask, jsonify, request,send_from_directory
from flask_cors import CORS
import mysql.connector as mysql
import os
import json