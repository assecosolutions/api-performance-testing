import time
from locust import HttpUser, task, between


class NodeJSExpressScenario01(HttpUser):
    host = 'http://afpt-node-js-express-scenario-01'
    wait_time = between(2, 4)

    @task
    def hello(self):
        self.client.get("/api/hello?name=Armen",
                        name="NodeJSExpressScenario01")


class NodeJSNestJsExpressScenario01(HttpUser):
    host = 'http://afpt-node-js-nestjs-express-scenario-01'
    wait_time = between(2, 4)

    @task
    def hello(self):
        self.client.get("/api/hello?name=Armen", name="NodeJSNestJsScenario01")

class NodeJSNestJsFastifyScenario01(HttpUser):
    host = 'http://afpt-node-js-nestjs-fastify-scenario-01'
    wait_time = between(2, 4)

    @task
    def hello(self):
        self.client.get("/api/hello?name=Armen", name="NodeJSNestJsFasitfyScenario01")
        
class RustRocketScenario01(HttpUser):
    host = 'http://afpt-rust-rocket-scenario-01'
    wait_time = between(2, 4)

    @task
    def hello(self):
        self.client.get("/api/hello?name=Armen", name="RustRocketScenario01")
