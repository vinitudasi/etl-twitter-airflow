# 📊 Data Engineering Project with Airflow

This project demonstrates a simple **ETL pipeline** for extracting tweets using the Twitter API, transforming the data, and loading it into an Amazon S3 bucket. The entire workflow is orchestrated using **Apache Airflow**.

It is based on the YouTube series by Darshil Parmar: [Airflow Project Tutorial](https://www.youtube.com/watch?v=q8q3OFFfY6c).

## 🛠️ Tech Stack
- **Apache Airflow**: Workflow orchestration
- **Python**: Scripting & ETL logic
- **Tweepy**: Twitter API wrapper
- **Pandas**: Data processing
- **Amazon S3**: Data lake storage
- **dotenv**: Environment variable management

## 📁 File Structure
```
├── dags/
│   └── twitter_dag.py         # Airflow DAG definition
├── twitter_etl.py             # ETL logic to fetch and process tweets
├── .env                       # Environment variables (not uploaded to GitHub)
└── README.md                  # Project documentation
```

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/vinitudasi/etl-twitter-airflow.git
cd etl-twitter-airflow
```

### 2. Create a `.env` file
```env
TWITTER_CONSUMER_KEY=your_key
TWITTER_CONSUMER_SECRET=your_secret
TWITTER_ACCESS_KEY=your_access_key
TWITTER_ACCESS_SECRET=your_access_secret
S3_BUCKET=s3://your-bucket-name/
EMAIL=your-email@example.com
```

### 3. Install dependencies
You should have Apache Airflow installed and configured. Also install:
```bash
pip install pandas tweepy python-dotenv
```

### 4. Setup DAG in Airflow
- Move `twitter_dag.py` into your Airflow `dags/` directory.
- Ensure `twitter_etl.py` is in the same directory or accessible via import.
- Start Airflow scheduler & webserver:
```bash
airflow scheduler
airflow webserver
```
- Visit `http://localhost:8080`, activate the `twitter_dag` DAG.

## 📦 Output
A CSV file containing the last 100 tweets from Elon Musk will be saved to your configured S3 bucket as `elonmusk_twitter_data.csv`.

## 📌 Notes
- Make sure your Twitter Developer account is approved.
- You may need to configure AWS CLI or boto3 permissions for writing to S3.
- This project uses basic error handling. For production, add retries and logging.

## 📧 Contact
For any questions, feel free to reach out at [vinitudasi8888@gmail.com](vinitudasi8888@gmail.com).

---
Made with ❤️ using Airflow and Python.
