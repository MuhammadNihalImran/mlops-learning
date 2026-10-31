import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("MLOps project started")
logging.warning("Dataset is relatively small")
logging.error("Example error message")