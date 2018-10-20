import logging

from django.shortcuts import render

# Create your views here.
logger = logging.getLogger(__name__)


def create_file(request):
    logger.info("create_file")


def update_file(request):
    logger.info("update_file")


def delete_file(request):
    logger.info("delete_file")


def create_folder(request):
    logger.info("create_folder")


def update_folder(request):
    logger.info("update_folder")


def delete_folder(request):
    logger.info("delete_folder")
