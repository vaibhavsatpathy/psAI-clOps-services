from psAI_clOps_datahub.base import client


def get_all_models(num_of_models: int = 10):
    try:
        models = []
        for i in range(num_of_models):
            try:
                data = dict(client.get_experiment(experiment_id=i))
                data["swagger_url"] = "https://bentoml.smartbox-capture.com/"
                models.append(data)
            except:
                pass
        return models
    except:
        return "Couldn't fetch the essential data"


def get_model_desc(experiment_name: str):
    try:
        data = client.search_runs(
            [client.get_experiment_by_name(name=experiment_name).experiment_id]
        )
        all_runs = []
        for runs in data:
            meta_data = runs.data
            info = dict(runs.info)
            metrics = dict(meta_data.metrics)
            params = dict(meta_data.params)
            run_dict = {
                "metrics": metrics,
                "params": params,
                "info": info,
                "swagger_url": "https://bentoml.smartbox-capture.com/",
            }
            all_runs.append(run_dict)
        return all_runs
    except:
        return "Couldn't fetch the essential data"
