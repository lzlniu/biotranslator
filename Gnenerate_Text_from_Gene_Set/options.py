class options:
    def __init__(self):
        self.raw_path = '../data/goa_human_raw/goa_human_data.pkl'
        self.model_name = 't5-base'
        self.device_0 = 'cuda:0'
        self.tokenizer_path = '/disk1/hwxu/hugging_face_model/' + self.model_name + '/'
        self.model_path = '/disk1/hwxu/hugging_face_model/' + self.model_name + '/'
        self.save_model = 'results/model/goa_human_textomics_cl_fold_{}.pkl'
        self.logger_name = 'results/training_log/textomics_cl.log'
        self.save_metrics = 'results/metrics/goa_human_eval_cl_fold_{}.pkl'
        self.nst_metrics = 'results/metrics/goa_human_nst_fold_{}.pkl'
        self.save_test_text = 'results/save_test_text/goa_human_cl_fold_{}_epoch_{}.csv'
        self.cl = False
        self.cl_d = 64
        self.cl_beta = 1
        self.K = 5
        self.max_length = 64
        self.test_size = 0.2
        self.exclude_jac = 0.5  # no exclude with setting 1
        self.nFold = 5
        self.batch_size = 16
        self.epoch = 15
        self.h = 1
        self.d_a = 8
        self.tau = 0.1
        self.lr = 0.0001
        self.num_beams = 2
        self.repetition_penalty = 2.5
        self.length_penalty = 1.0
        self.eval_interval = 3
        self.num_warmup_steps = 200
