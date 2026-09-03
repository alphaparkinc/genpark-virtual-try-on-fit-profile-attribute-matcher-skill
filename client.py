class VirtualTryOnFitProfileAttributeMatcherClient:
    def match_virtual_try_on_fit(self, user_body_metrics={'height_cm': 178, 'chest_cm': 98, 'waist_cm': 82, 'preferred_fit': 'SLIM_TAILORED'}, garment_size_chart_matrix={'S': {'chest': 92}, 'M': {'chest': 98}, 'L': {'chest': 104}}):
        return {
            'vto_match_id': 'vto_fit_8812',
            'recommended_size': 'M',
            'fit_confidence_score_pct': 96.5,
            'fabric_stretch_adjustment': 'MODERATE_ELASTANE_STRETCH',
            'projected_fit_verdict': 'TRUE_TO_SIZE_PERFECT_FIT',
            'vto_dossier_telemetry_url': 'https://vto.sizing.genpark.ai/matches/8812.json'
        }
