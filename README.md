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

|Type|Name                         |Request Count|Failure Count|Median Response Time|Average Response Time|Min Response Time |Max Response Time |Average Content Size|Requests/s         |Failures/s         |50%|66%|75%|80%|90%|95%|98%|99%|99.9%|99.99%|100%|
|----|-----------------------------|-------------|-------------|--------------------|---------------------|------------------|------------------|--------------------|-------------------|-------------------|---|---|---|---|---|---|---|---|-----|------|----|
|GET |NodeJSExpressScenario01      |11           |1            |3                   |3.837990909085482    |1.7951999999752388|11.27629999999158 |10.0                |0.37346824078480445|0.03395165825316404|3  |3  |4  |4  |8  |11 |11 |11 |11   |11    |11  |
|GET |NodeJSNestJsFasitfyScenario01|9            |9            |2                   |1.862799999994675    |1.4567000000056396|2.9399999999952797|0.0                 |0.30556492427847637|0.30556492427847637|2  |2  |2  |2  |3  |3  |3  |3  |3    |3     |3   |
|GET |NodeJSNestJsScenario01       |11           |11           |2                   |1.720945454541772    |1.4381999999955042|2.2372999999902277|0.0                 |0.37346824078480445|0.37346824078480445|2  |2  |2  |2  |2  |2  |2  |2  |2    |2     |2   |
|    |Aggregated                   |31           |21           |2                   |2.5133387096726407   |1.4381999999955042|11.27629999999158 |3.5483870967741935  |1.0525014058480853 |0.7129848233164449 |2  |2  |3  |3  |3  |8  |11 |11 |11   |11    |11  |
