from clipper_admin import ClipperConnection, KubernetesContainerManager
clipper_conn = ClipperConnection(KubernetesContainerManager(useInternalIP=True))
clipper_conn.connect()

