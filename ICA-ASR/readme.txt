Dataset to evaluate eye artifact correction algorithms in electroencephalographic (EEG) data as presented in [1].

**Description**

The dataset contains pre-processed EEG recordings of 4 EEG studies [2-5], including a total of 45 sessions with 39 participants. 
During each session, two blocks of eye artifact (eye movements and blinks) and resting activity were recorded according to the paradigm presented in [1,2]. The detailed experimental setup as well as the pre-processing steps are presented in [1].

**Dataset structure**

The recordings of study <code>i</code> are stored in distinct folder <code>study0i</code>.
The participant ids are unique across all studies; e.g., the id of the first participant is <code>p01</code>.
The study id and participant id identify the recordings associated to a session. The files associated to a session start with the prefix <code>study0i_p0j_</code>.

Each session contains 3 files <code>..._prep.set</code>,  <code>..._prep.fdt</code> and  <code>..._block_dt.mat</code>.
The <code>.set/.fdt</code> files contain the pre-processed EEG data in the eeglab format [6]. The data is organized in a <code>n_channels x n_samples x n_trials</code> tensor. The labelsand type of each channel is stored in the field <code>chanlocs</code>. EOG and EEG channels have the type <code>EEG</code>. EOG derivatives have the type <code>EOG</code>.

The channel with the label <code>label</code> and type <code>STATE</code> contains the trial label.
Four trial labels are possible:
<pre>
1 ... rest trial
2 ... horizontal eye movement trial
3 ... vertical eye movement trial
4 ... blink trial
</pre>

The channel with the label <code>artifactclasses</code> and type <code>LABEL</code> contains the sample labels.
Each sample can have the following labels:
<pre>
1 ... rightwards eye movement
2 ... leftwards eye movement
3 ... upwards eye movement
4 ... downwards eye movement
5 ... blink
6 ... resting activity
0 ... none
</pre>

The experimental block (1 or 2) is encoded in the channel with the label <code>block</code> and type <code>PARADIGM</code>. The start time-stamps of both blocks are stored in the <code>.mat</code> file.

**References**

[1] Kobler, R. J., Sburlea, A. I., Lopes-Dias, C., Schwarz, A., Hirata, M. & Müller-Putz, G. R. "Corneo-retinal-dipole and blink related eye artifacts can be corrected offline and online in electroencephalographic and magnetoencephalographic signals", in preparation

[2] Kobler, R. J., Sburlea, A. I., and Müller-Putz G.R., "A Comparison of Ocular Artifact Removal Methods for Block Design Based Electroencephalography Experiments." In Proceedings of the 7th Graz Brain-Computer Interface Conference, 236–41, 2017. https://doi.org/10.3217/978-3-85125-533-1-44.

[3] Kobler, R. J., Sburlea, A. I., and Müller-Putz., G. R. "Tuning Characteristics of Low-Frequency EEG to Positions and Velocities in Visuomotor and Oculomotor Tracking Tasks." Scientific Reports 8, no. 1 (2018): 17713. https://doi.org/10.1038/s41598-018-36326-y.

[4] Mondini, V., Kobler, R.J., Sburlea, A.I., and Müller-Putz G.R. "Online EEG Based Decoding of Arm Movement for the Natural Control of an Assistive Robotic Arm," in preparation.

[5] Lopes-Dias, C., Sburlea, A.I., and Müller-Putz, G.R. "Online Asynchronous Decoding of Error-Related Potentials during the Continuous Control of a Robot." Scientific Reports 9, no. 1 (2019): 17596. https://doi.org/10.1038/s41598-019-54109-x.

[6]Delorme, A., and Makeig, S. "EEGLAB: An Open Source Toolbox for Analysis of Single-Trial EEG Dynamics Including Independent Component Analysis." Journal of Neuroscience Methods 134, no. 1 (2004): 9–21. https://doi.org/10.1016/j.jneumeth.2003.10.009.



