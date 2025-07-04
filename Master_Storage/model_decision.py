import logging

from supplychainpy.bi._analytical_heirachy_process import _PairwiseComparison

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def analytical_hierarchy_process(criteria: tuple, criteria_scores: list, options: tuple, option_scores: dict,
                                 quantitative_criteria: tuple = None, **kwargs):
    """ Compute an analytical hierarchy for alternative choices based on relative weights and priorities of categories.

    Args:
        criteria (tuple):                List the criteria to base decision between alternative choices.
        criteria_scores (list):          List the scores for the criteria as a list of tuples, the reciprocals are
                                         auto-calculated.
        options (tuple):                 The alternative otpions to decide between.
        option_scores (dict):            A dict of tuples scoring the alternatives. The tuple order must mirror the
                                         'alternative' argument tuple.
        quantitative_criteria (tuple):   List the quantitative criteria e.g. 'fuel economy', that use representative
                                         values and not scores
        **kwargs:
            item_cost (dict):   A dict of alternatives and their corresponding costs. Only necessary if seeking to use cost benefit ratios for further discretion.

    Returns:
        dict:   Summary of analytical hierarchy and cost benefit analysis if kwargs 'item_cost' used.

    Examples:

    >>> lorry_cost = {'scania': 68000,'iveco': 79000,'volvo': 59000,'navistar': 66000}
    >>> criteria = ('style', 'reliability', 'fuel_economy')
    >>> criteria_scores = [(1, 1 / 2, 3), (0, 1, 4), (0, 0, 1)]
    >>> options = ('scania', 'iveco', 'volvo', 'navistar')
    >>> options_scores ={'reliability': [(1, 2, 5, 1), (1 / 2, 1, 3, 2), (1 / 5, 1 / 3, 1, 1 / 4), (1, 1 / 2, 4, 1)],
    ...     'style': [(1, 1 / 4, 4, 1 / 6), (4, 1, 4, 1 / 4),(1 / 4, 1 / 4, 1, 1 / 5), (6, 4, 5, 1)],
    ...     'fuel_economy': (62, 55, 56, 56)}
    >>> lorry_decision = analytical_hierarchy_process(criteria= criteria, criteria_scores=criteria_scores,
    ...     options= options, option_scores=options_scores, quantitative_criteria=('fuel_economy',),
    ...     item_cost = lorry_cost)

    """
    ahp = _PairwiseComparison(criteria=criteria,
                              criteria_scores=criteria_scores,
                              options=options,
                              option_scores=option_scores,
                              quantitative_criteria=quantitative_criteria)
    if kwargs:
        ahp_cvb = ahp.cost_benefit_summary(ahp_summary=ahp.summary(), item_cost=kwargs.get('item_cost'))
        log.debug("AHP completed")
        return {'analytical_hierarchy': ahp.summary(), 'cost_benefit_ratios': ahp_cvb}

    return ahp.summary()
