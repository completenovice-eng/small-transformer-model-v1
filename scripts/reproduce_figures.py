# SPDX-License-Identifier: MIT
# Copyright (c) 2026 completenovice-eng
"""Reproduce P1 figures from public aggregates only. No model code, network or weights."""
import argparse,csv,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read_rows(p):
 with p.open(newline='') as f:return list(csv.DictReader(f))
def draw(output, rows):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.colors import TwoSlopeNorm
    from matplotlib.patches import FancyBboxPatch
    if matplotlib.__version__ != '3.10.7' or np.__version__ != '2.2.6':
        raise RuntimeError('PLOT_ENVIRONMENT_VERSION_MISMATCH')

    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                         'axes.spines.top': False, 'axes.spines.right': False,
                         'svg.hashsalt': 'model-v1-obs5-p1', 'svg.fonttype': 'none',
                         'savefig.facecolor': 'white'})
    directory = output / 'figures'
    directory.mkdir(exist_ok=True)
    inventory = []

    def save(fig, number, name, datasets, method, limits):
        fig.text(.01, .006, 'OBS-5 interim report | descriptive measurements | scientific Primary approval: 0',
                 fontsize=8, color='#505050')
        for ext in ['svg', 'png']:
            metadata = {'Date': None, 'Creator': 'Model v1 P1 saved-data plotting'} if ext == 'svg' else {'Software': 'Model v1 P1 saved-data plotting'}
            fig.savefig(directory / f'fig{number:02d}_{name}.{ext}', dpi=150, metadata=metadata,
                        bbox_inches='tight', pad_inches=.18)
            if ext == 'svg':
                p = directory / f'fig{number:02d}_{name}.{ext}'
                # Matplotlib emits trailing spaces in multiline path coordinates.
                # Keep newline separators; XML geometry/text values are unchanged.
                p.write_text('\n'.join(line.rstrip() for line in p.read_text().splitlines())+'\n')
        plt.close(fig)
        inventory.append({'figure_id': f'Figure {number}', 'name': name,
                          'data_files': datasets, 'method': method, 'limitations': limits,
                          'outputs': {f'figures/fig{number:02d}_{name}.{e}': digest(directory / f'fig{number:02d}_{name}.{e}') for e in ['svg', 'png']}})

    # 1: Method-history schematic. Widths encode no duration/effect size.
    fig, ax = plt.subplots(figsize=(12, 6.5))
    ax.set(xlim=(0, 3), ylim=(0, 3.4)); ax.axis('off')
    stages = [('Original question', 'Experience X -> ability Y\nTiming, transfer, internal changes\n2209bb1'),
              ('Native-format audit', 'No unique answer continuation\nPrimary feasibility 0/36\n15019fa'),
              ('Paired eval-only readout', '27,543 retained blocks / 36 cells\nScientific Primary approval 0\n0dac478 / 5cee366'),
              ('Positive calibration', 'Original: 36/1,024 correct\nLimited heldout: 38/512\n0ae379c / da3fcf0'),
              ('Scope transition', 'Descriptive observation\nOriginal goal/history retained\n1925d25'),
              ('OBS-5 interim result', '10M/MIX/r0 completed\n1 of 15 planned trajectories\n1760d24')]
    for i, (title, text) in enumerate(stages):
        x, y = i % 3 + .06, 2.05 - (i // 3) * 1.55
        ax.add_patch(FancyBboxPatch((x, y), .87, 1.15, boxstyle='round,pad=.025',
                                   facecolor='#edf3f8' if i < 4 else '#f7eddb', edgecolor='#62798b'))
        ax.text(x + .05, y + .95, f'{i + 1}. {title}', weight='bold', fontsize=10)
        ax.text(x + .05, y + .72, text, va='top', fontsize=9, linespacing=1.6)
    ax.set_title('Figure 1. Research and measurement decisions (schematic; no time scale)', pad=20)
    save(fig, 1, 'research_history', ['research_evidence_ledger'], 'Selected decision milestones F001/F022/F030/F031/F043/F053/F057/F067; commit order.', 'Not an effect or duration plot; full decision history remains in H2.')

    # 2: Frozen design vs actual execution.
    fig, ax = plt.subplots(figsize=(10, 4.6))
    conditions = ['MIX', 'PURE-LOGIC', 'PURE-MATH', 'PURE-CODE', 'PURE-NATURAL']
    matrix = np.zeros((3, 5)); matrix[0, 0] = 1
    ax.imshow(matrix, cmap=matplotlib.colors.ListedColormap(['#edf0f3', '#357ba3']), vmin=0, vmax=1)
    ax.set_xticks(range(5), conditions); ax.set_yticks(range(3), ['10M', '20M', '30M'])
    for i in range(3):
        for j in range(5):
            ax.text(j, i, 'COMPLETED\nr0 / exact 2B' if matrix[i, j] else 'NOT STARTED\ndesign approved',
                    ha='center', va='center', color='white' if matrix[i, j] else '#334155', fontsize=9)
    ax.set_title('Figure 2. Approved design: 15 trajectories; observed: 1 trajectory\nSame-size initial state group; cross-size stream sharing within condition/r0')
    fig.tight_layout(rect=(0, .04, 1, 1))
    save(fig, 2, 'condition_matrix', ['condition_matrix'], 'All 5 conditions x 3 widths, replicate0. Actual OBS5 overlay only for10M/MIX.', 'Remaining14 results are unavailable; design approval is not execution permission.')

    # 3: No invented loss at update0; no moving-window parameter selected after results.
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.7), sharey=True)
    train = [r for r in rows['training_intervals'] if r['interval_N']]
    for ax in axes:
        for r in train:
            a = (int(r['interval_start_update']) - 1) * 32704 / 1e9
            b = int(r['predictions']) / 1e9
            ax.hlines(float(r['interval_mean_loss']), a, b, color='#267a9b', linewidth=2)
        ax.scatter([int(r['predictions']) / 1e9 for r in train], [float(r['endpoint_batch_loss']) for r in train],
                   s=19, color='#bc6735', marker='x', label='Endpoint batch loss')
        ax.plot([], [], color='#267a9b', linewidth=2, label='Nonoverlapping interval mean')
        ax.set(xlim=(0, 2.000045824), ylim=(0, 10), xlabel='Loss-bearing predictions (billions)')
        ax.grid(alpha=.18)
    axes[0].set_ylabel('Next-token cross-entropy (nats / prediction)')
    axes[0].set_title('Full horizon, linear prediction axis')
    axes[1].set_xscale('symlog', linthresh=.001)
    axes[1].set_title('Same data, symlog prediction axis (linear <=0.001B)')
    axes[1].legend(fontsize=8, loc='upper right')
    fig.suptitle('Figure 3. 10M/MIX/r0 training loss | 61,156 updates / 24 fixed intervals\nUpdate0 training loss: not applicable; no values imputed')
    fig.tight_layout(rect=(0, .04, 1, .91))
    save(fig, 3, 'training_loss', ['training_intervals'], '24 fixed checkpoint intervals cover61156 equal-size updates; horizontal means and endpoint batch dots; y includes0.', 'Different batches across updates; not task competence; axis transform explicitly shown.')

    # 4: Different token distributions; do not rank domain abilities by raw NLL.
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.7), sharey=True)
    probe = rows['probe_nll']
    for ax in axes:
        for domain, color in zip(['natural', 'math', 'logic', 'code'], ['#b66a2a', '#7655a3', '#287f8e', '#467e3b']):
            ax.plot([int(r['predictions']) / 1e9 for r in probe], [float(r[domain + '_NLL']) for r in probe],
                    'o-', label=domain, color=color, linewidth=1, markersize=3)
        ax.set(xlim=(0, 2.000045824), ylim=(0, 10), xlabel='Loss-bearing predictions (billions)')
        ax.grid(alpha=.18)
    axes[0].set_ylabel('Fixed-probe mean NLL (nats / prediction)')
    axes[0].set_title('Full horizon, linear prediction axis')
    axes[1].set_xscale('symlog', linthresh=.001); axes[1].set_title('Same data, symlog prediction axis')
    axes[1].legend(fontsize=8)
    fig.suptitle('Figure 4. Domain probe NLL | 25 checkpoints, 32,704 probe predictions/domain/point\nDifferent domain distributions; line segments are visual guides, not continuous measurements')
    fig.tight_layout(rect=(0, .04, 1, .91))
    save(fig, 4, 'probe_nll', ['probe_nll'], '25 saved metrics per domain, no new per-token likelihood calculation. Both axes include0.', 'Domain NLL values have different reference distributions; not comparable domain capability scores.')

    cells = sorted({r['cell_id'] for r in rows['cell_trajectories']})
    times = sorted({int(r['update']) for r in rows['cell_trajectories']})
    lookup = {(r['cell_id'], int(r['update'])): r for r in rows['cell_trajectories']}
    labels = [f"{c} (N={lookup[c, times[0]]['N']})" for c in cells]
    margins = np.array([[float(lookup[c, u]['mean_margin']) for u in times] for c in cells])
    pairs = np.array([[float(lookup[c, u]['pair_correct_fraction']) for u in times] for c in cells])
    ticklabels = [f'{u:,}\n{u * 32704 / 1e9:.5f}B' for u in times]

    fig, ax = plt.subplots(figsize=(12, 13))
    vmax = float(np.abs(margins).max())
    image = ax.imshow(margins, aspect='auto', cmap='RdBu_r', norm=TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax))
    ax.set_yticks(range(36), labels, fontsize=8); ax.set_xticks(range(9), ticklabels, fontsize=8)
    ax.set_xlabel('Update / cumulative predictions (equally spaced columns; unequal time intervals)')
    ax.set_title('Figure 5. All36 cells /9 Full points: equal-block mean paired margin (nats)\n10M/MIX/r0; DESCRIPTIVE_ONLY; one training replicate; no seed-level CI')
    fig.colorbar(image, ax=ax, label='Mean paired margin (nats; shared symmetric scale)')
    fig.tight_layout(rect=(0, .04, 1, 1))
    save(fig, 5, 'paired_margin_all_cells', ['cell_trajectories'], '36x9 exact saved cell means; one symmetric global color scale; all cells retained.', 'N is retained distinct block count, not proven statistical independence. No per-row normalization; no capability threshold.')

    fig, axes = plt.subplots(3, 1, figsize=(12.5, 18), gridspec_kw={'height_ratios': [7, 1.8, 1.4]})
    im = axes[0].imshow(pairs, aspect='auto', cmap='Blues', vmin=0, vmax=1)
    axes[0].set_yticks(range(36), labels, fontsize=8); axes[0].set_title('A. Target strict PAIR_CORRECT fraction | same36 cells')
    fig.colorbar(im, ax=axes[0], label='Strict both-side candidate-selection fraction (0..1)')
    groups = sorted({r['control_group'] for r in rows['interface_controls']})
    ctrl = {(r['control_group'], int(r['update'])): r for r in rows['interface_controls']}
    data = np.array([[float(ctrl[g, u]['pair_correct_fraction']) for u in times] for g in groups])
    im = axes[1].imshow(data, aspect='auto', cmap='Blues', vmin=0, vmax=1)
    axes[1].set_yticks(range(5), [g+' (N=256)' for g in groups], fontsize=8)
    axes[1].set_title('B. Literal lookup controls | no pass threshold applied')
    fig.colorbar(im, ax=axes[1], label='Strict both-side selection fraction (0..1)')
    kinds = ['RENDERER', 'SHAM_COUNTERFACTUAL']
    diag = {(r['diagnostic_kind'], int(r['update'])): r for r in rows['negative_diagnostics']}
    data = np.array([[float(diag[g, u]['mean_absolute_preference_change']) for u in times] for g in kinds])
    im = axes[2].imshow(data, aspect='auto', cmap='YlOrBr', vmin=0)
    axes[2].set_yticks(range(2), [g+' (N=1,027 views)' for g in kinds], fontsize=8)
    axes[2].set_title('C. Same-truth nuisance: mean absolute candidate-preference change\nPOSITION is bookkeeping only: 1,027/1,027 valid per point; no numeric null statistic')
    fig.colorbar(im, ax=axes[2], label='Absolute preference change (nats)')
    for ax in axes:
        ax.set_xticks(range(9), ticklabels, fontsize=8)
    axes[2].set_xlabel('Update / cumulative predictions (equally spaced columns)')
    fig.suptitle('Figure 6. Targets, controls and diagnostics | 10M/MIX/r0 | descriptive only\nNo PAIR_CORRECT chance=0.25 assumption; nuisance views add no independent target N', y=.999)
    fig.tight_layout(rect=(0, .03, 1, .98))
    save(fig, 6, 'selection_controls_diagnostics', ['cell_trajectories', 'interface_controls', 'negative_diagnostics'], 'All36 target fractions, five literal-control groups and two nuisance summaries. Position diagnostic reported as bookkeeping, not imputed zero.', 'Controls do not prove rule semantics; 79 identical shams; no formal expected-zero null; views are dependent.')

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.9), sharey=True)
    trajectory = rows['limited_m3_trajectory']
    for key, n, color, label in [('fit_exact', 512, '#287f8e', 'Training fit (N=512 sides)'), ('development_exact', 256, '#b66a2a', 'Development (N=256 sides)')]:
        axes[0].plot([r['predictions'] / 1e6 for r in trajectory], [r[key] / n * 100 for r in trajectory], 'o-', color=color, label=label)
    axes[0].scatter([50.004416], [38 / 512 * 100], color='#a63253', marker='D', s=55, label='Final heldout (N=512 sides)', zorder=4)
    axes[0].set(xlim=(0, 51), xlabel='Calibration predictions (millions)', ylabel='Exact oracle correctness (%)', ylim=(0, 105))
    axes[0].legend(fontsize=8, loc='center right'); axes[0].grid(alpha=.18)
    vals = [511/512*100, 34/256*100, 38/512*100]
    axes[1].bar(['Fit\n511/512', 'Development\n34/256', 'Heldout\n38/512'], vals, color=['#287f8e', '#b66a2a', '#a63253'])
    axes[1].axhline(90, color='#555555', linestyle=':', label='90% exact-side condition (not sufficient alone)')
    axes[1].legend(fontsize=7, loc='upper right'); axes[1].set_title('Final update1,529; equal fixed training budget')
    axes[1].text(.02, .40, 'Heldout strict generation pairs: 0/256\nPOSITIVE_NOT_ESTABLISHED\nStage C paired scorer: NOT_RUN', transform=axes[1].transAxes, fontsize=9,
                 bbox={'facecolor': 'white', 'alpha': .9, 'edgecolor': 'none', 'pad': 5})
    fig.suptitle('Figure 7. Limited M3 calibration | one fresh20M / one seed / one run\n50,004,416 predictions; high fit does not establish world-disjoint competence')
    fig.tight_layout(rect=(0, .04, 1, .89))
    save(fig, 7, 'limited_m3_calibration', ['limited_m3_trajectory', 'limited_m3_terminal'], 'Fixed0/382/764/1146/1529 fit/dev observations and terminal-only world-disjoint heldout. Full0..100% scale.', '0/256 is independent generation pairs, not paired scorer; overlapping conflict strata not extra N; no causal memorization diagnosis.')
    return inventory
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
 args.output.mkdir(parents=True,exist_ok=False)
 names=['training_intervals','probe_nll','cell_trajectories','interface_controls','negative_diagnostics','condition_matrix','limited_m3_trajectory','limited_m3_terminal']
 rows={n:read_rows(ROOT/'data'/(n+'.csv')) for n in names}
 rows['limited_m3_trajectory']=[{k:int(v) for k,v in r.items()} for r in rows['limited_m3_trajectory']]
 figs=draw(args.output,rows)
 (args.output/'reproduction.json').write_text(json.dumps({'status':'SAVED_AGGREGATE_REPRODUCTION_ONLY','model_forwards':0,'figures':figs},sort_keys=True,indent=2)+'\n')
if __name__=='__main__':main()
