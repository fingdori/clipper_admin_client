
def main(version, label):
    from clipper_admin import ClipperConnection, KubernetesContainerManager
    clipper_conn = ClipperConnection(KubernetesContainerManager(useInternalIP=True))
    clipper_conn.connect()
    from clipper_admin.deployers import python as python_deployer
    registry='localhost:5000'
    python_deployer.deploy_python_closure(clipper_conn, name="sum-model", version=version, input_type="doubles", func=feature_sum,
            labels=[label], registry=registry)

def feature_sum(xs):
    return [str(sum(x)) for x in xs]

import sys

if __name__ == "__main__":
    # execute only if run as a script
    print("argument length : {}".format(len(sys.argv)))
    
    print(sys.argv[1])
    print(sys.argv[2])
    main(sys.argv[1], sys.argv[2])
