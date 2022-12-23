# 🏃🏼‍♂️⏱️ Performance Comparison - API Frameworks

The purpose of this repository is to compare the performance of different API framework. The results can and shall be used as a basis for future decions.

## 🧪 How the Performance Is Tested

To get insights about the performance of a framework we are using [`Locust`](https://locust.io/). Locust is an open source load testing tool.

The following frameworks will be considered within the load test:

**Node:**

- [express](https://expressjs.com/de/)
- [Nest.js (express)](https://nestjs.com/)
- [Nest.js (fastify)](https://nestjs.com/)

**Rust:**

- [Rocket](https://rocket.rs/)

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

|Type|Name                         |Request Count|Failure Count|Median Response Time|Average Response Time|Min Response Time |Max Response Time |Average Content Size|Requests/s        |Failures/s        |50%|66%|75% |80% |90% |95% |98% |99% |99.9%|99.99%|100%|
|----|-----------------------------|-------------|-------------|--------------------|---------------------|------------------|------------------|--------------------|------------------|------------------|---|---|----|----|----|----|----|----|-----|------|----|
|GET |NodeJSExpressScenario01      |9            |0            |3                   |5.877222222224532    |1.8776000000002568|32.81129999999166 |11.0                |0.3976156251762339|0.0               |3  |3  |3   |3   |33  |33  |33  |33  |33   |33    |33  |
|GET |NodeJSNestJsFasitfyScenario01|8            |8            |2                   |2.0314125000009398   |1.4747999999968897|2.5667000000026974|0.0                 |0.3534361112677635|0.3534361112677635|2  |2  |2   |2   |3   |3   |3   |3   |3    |3     |3   |
|GET |NodeJSNestJsScenario01       |8            |8            |2                   |1.8961749999988342   |1.430700000000229 |3.0198000000041247|0.0                 |0.3534361112677635|0.3534361112677635|2  |2  |2   |2   |3   |3   |3   |3   |3    |3     |3   |
|GET |RustRocketScenario01         |6            |6            |10                  |682.0000000000022    |5.82630000000961  |3039.1772999999916|0.0                 |0.2650770834508226|0.2650770834508226|12 |12 |1000|1000|3000|3000|3000|3000|3000 |3000  |3000|
|    |Aggregated                   |31           |22           |2                   |134.71986129032362   |1.430700000000229 |3039.1772999999916|3.193548387096774   |1.3695649311625835|0.9719493059863495|2  |3  |3   |6   |12  |1000|3000|3000|3000 |3000  |3000|
