# 🏃🏼‍♂️⏱️ Performance Comparison - API Frameworks

The purpose of this repository is to compare the performance of different API framework. The results can and shall be used as a basis for future decions.

## 🧪 How the Performance Is Tested

To get insights about the performance of a framework we are using [`Locust`](https://locust.io/). Locust is an open source load testing tool.

The following frameworks will be considered within the load test:

**Node:**

- [express](https://expressjs.com/de/)
- [Nest.js (express)](https://nestjs.com/)
- [Nest.js (fastify)](https://nestjs.com/)

### 🌄 Scenarios

We will provide different scenarios of complexity from simple to very complex which will be implemented by every framework. The scenarios are described below.

#### 01 - Simplest Possible API

All of the frameworks which are under test have to provide an endpoint (`/api/hello`). The endpoint should be capable of returning a greeting phrase for a certain person by sending a `GET` request to the endpoint `/api/hello`. The name of the person should be defined by providing an query parameter with the name. Which than looks like this: `/api/hello?name=Armen`.

## 🧑🏼‍🔬 How You Can Get the Tests Results

If you would like to carry out the tests by yourself please carry out the following steps.

1. Clone this repository to your local machine by running `git clone https://github.com/assecosolutions/api-performance-testing.git`
2. Navigate to the root folder of this project and execute `docker-compose up`. Now the load tests will automatically run. They will be finished after around `30s`. After they ran you can stop the `docker-compose up` command.
3. The results of the load test can be found in the `tests/results` directory.

## 📝 Performance Testing Results

| Type | Name                    | Request Count | Failure Count | Median Response Time | Average Response Time | Min Response Time | Max Response Time  | Average Content Size | Requests/s         | Failures/s          | 50% | 66% | 75% | 80% | 90% | 95% | 98% | 99% | 99.9% | 99.99% | 100% |
| ---- | ----------------------- | ------------- | ------------- | -------------------- | --------------------- | ----------------- | ------------------ | -------------------- | ------------------ | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ---- |
| GET  | NodeJSExpressScenario01 | 10            | 0             | 3                    | 4.638830485055223     | 2.248245000373572 | 20.227878994774073 | 11.0                 | 0.3496365148314121 | 0.0                 | 3   | 3   | 4   | 4   | 20  | 20  | 20  | 20  | 20    | 20     | 20   |
| GET  | NodeJSNestJsScenario01  | 10            | 3             | 4                    | 4.5807313930708915    | 2.069005975499749 | 14.483044971711934 | 7.7                  | 0.3496365148314121 | 0.10489095444942363 | 4   | 4   | 5   | 5   | 14  | 14  | 14  | 14  | 14    | 14     | 14   |
|      | Aggregated              | 20            | 3             | 3                    | 4.609780939063057     | 2.069005975499749 | 20.227878994774073 | 9.35                 | 0.6992730296628242 | 0.10489095444942363 | 3   | 4   | 4   | 5   | 14  | 20  | 20  | 20  | 20    | 20     | 20   |
