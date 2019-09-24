

from clipper_admin import ClipperConnection, KubernetesContainerManager
clipper_conn = ClipperConnection(KubernetesContainerManager(useInternalIP=True))
clipper_conn.connect()

clipper_conn.register_application(name="hello-world", input_type="doubles", default_output="-1.0", slo_micros=100000)
clipper_conn.get_all_apps()

def feature_sum(xs):
    return [str(sum(x)) for x in xs]


from clipper_admin.deployers import python as python_deployer

registry = 'localhost:5000'
python_deployer.deploy_python_closure(clipper_conn, name="sum-model", version=1, input_type="doubles", func=feature_sum, registry=registry)

